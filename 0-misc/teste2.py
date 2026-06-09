from typing import List, Dict
import time

# --- Data Models ---

class HttpResponse:
    def __init__(self):
        self.status_code = 200


class DriverAvailability:
    def __init__(
        self,
        driver_id: int,
        start_min: int,
        end_min: int
    ):
        self.driver_id = driver_id
        self.start_min = start_min
        self.end_min = end_min


class ListDriverAvailabilityResponse(HttpResponse):
    def __init__(
        self,
        availabilities: List[DriverAvailability] = None
    ):
        super().__init__()
        self.availabilities = (
            availabilities if availabilities is not None else []
        )


# --- Mocked Downstream Service ---

class DriverApiService:
    def __init__(
        self,
        mocked_response: ListDriverAvailabilityResponse
    ):
        self.mocked_response = mocked_response

    def get_driver_availabilities(
        self,
        city_id: int
    ) -> ListDriverAvailabilityResponse:
        return self.mocked_response


# --- Core Service (to implement) ---

class DriverCapacityService:

    def __init__(
        self,
        driver_api: DriverApiService
    ):
        self.driver_api = driver_api

    def _mergeSort(self, windows):
        if len(windows) <= 1:
            return windows
        
        mid = len(windows) // 2

        left = self._mergeSort(windows[:mid])
        right = self._mergeSort(windows[mid:])

        return self._auxMerge(left, right)
    
    def _auxMerge(self, left, right):
        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def calculate_capacity(
        self,
        city_id: int
    ) -> List[Dict]:
        """
        Returns:

        List[Dict]:

        [
            {
                "start_min": int,
                "end_min": int,
                "capacity": int
            },
            ...
        ]

        Notes:

        - Availability windows are half-open intervals:
          [start_min, end_min)

        - Ignore invalid windows where:
          end_min <= start_min

        - Capacity represents the number of
          drivers available during a time range.

        - Adjacent intervals with the same
          capacity should be merged.
        """

        result: List[Dict] = []

        # TODO:
        # 1) Fetch availabilities from API
        # 2) Retry failed requests
        #
        
        resp = None
        retries = 3
        delay = 0.1

        for attempts in range(retries):
            try:
                resp = self.driver_api.get_driver_availabilities(city_id)
            except Exception:
                return []
            
            if resp and resp.status_code == 200:
                break
            elif attempts < retries - 1:
                time.sleep(delay)
                delay *= 2
            else:
                return []


        # 3) Filter invalid windows
        #

        valid: List[DriverAvailability] = []
        for availability in resp.availabilities:
            if availability.end_min > availability.start_min:
                valid.append(availability)
        
        if not valid:
            return []
        
        windows = []
        for k in valid:
            if k.start_min not in windows:
                windows.append(k.start_min)
            if k.end_min not in windows:
                windows.append(k.end_min)

        windows = self._mergeSort(windows)

        ranges = []
        for k in range(0, len(windows) - 1):
            ranges.append([windows[k], windows[k+1]])

        capacity: List[Dict] = []
        for k in ranges:
            dict_aux = {"start_min": k[0], "end_min": k[1], "capacity": 0}
            for driver in valid:
                if driver.start_min <= k[0] and driver.end_min >= k[1]:
                    dict_aux["capacity"] += 1
            if dict_aux["capacity"] > 0:
                capacity.append(dict_aux)

        if not capacity:
            return []
        
        # 5) Merge adjacent intervals that
        #    have the same capacity

        prev_capacity = capacity[0]["capacity"]
        capacities_merged: List[Dict] = []
        new_capacity = capacity[0]
        for k in range(1, len(capacity)):
            if capacity[k]["capacity"] != prev_capacity:
                capacities_merged.append(new_capacity)
                prev_capacity = capacity[k]["capacity"]
                new_capacity = capacity[k]
            else:
                new_capacity["end_min"] = capacity[k]["end_min"]
                new_capacity["capacity"] = capacity[k]["capacity"]


        capacities_merged.append(new_capacity)
        #
        # 6) Return consolidated timeline

        return capacities_merged


# --- Test Harness ---

def _print_result(
    test_name: str,
    expected,
    actual
):
    status = "PASS" if expected == actual else "FAIL"

    print(f"[{status}] {test_name}")
    print(f" Expected: {expected}")
    print(f" Actual: {actual}\n")


def test_capacity_aggregation():

    availabilities = [

        DriverAvailability(
            driver_id=1,
            start_min=60,
            end_min=180
        ),

        DriverAvailability(
            driver_id=2,
            start_min=120,
            end_min=240
        ),

        DriverAvailability(
            driver_id=3,
            start_min=150,
            end_min=210
        ),

        DriverAvailability(
            driver_id=4,
            start_min=500,
            end_min=500
        ),  # invalid

    ]

    mocked_api = DriverApiService(
        ListDriverAvailabilityResponse(
            availabilities
        )
    )

    service = DriverCapacityService(
        mocked_api
    )

    actual = service.calculate_capacity(
        city_id=123
    )

    expected = [

        {
            "start_min": 60,
            "end_min": 120,
            "capacity": 1
        },

        {
            "start_min": 120,
            "end_min": 150,
            "capacity": 2
        },

        {
            "start_min": 150,
            "end_min": 180,
            "capacity": 3
        },

        {
            "start_min": 180,
            "end_min": 210,
            "capacity": 2
        },

        {
            "start_min": 210,
            "end_min": 240,
            "capacity": 1
        }

    ]

    _print_result(
        "Aggregates driver capacity",
        expected,
        actual
    )


if __name__ == "__main__":
    test_capacity_aggregation()