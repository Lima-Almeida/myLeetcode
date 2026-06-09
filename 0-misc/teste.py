from typing import List, Dict
import time

# --- Data Models ---
class HttpResponse:
    def __init__(self):
        self.status_code = 200

class PickupWindow:
    def __init__(self, start_min: int, end_min: int):
        self.start_min = start_min
        self.end_min = end_min

class ListPickupWindowsResponse(HttpResponse):
    def __init__(self, windows: List[PickupWindow] = None):
        super().__init__()
        self.windows = windows if windows is not None else []

# --- Mocked Downstream Service ---
class KitchenConfigApiService:
    def __init__(self, mocked_response: ListPickupWindowsResponse):
        self.mocked_response = mocked_response

    def get_pickup_windows_for_restaurant(self, restaurant_id: int) -> ListPickupWindowsResponse:
        return self.mocked_response

# --- Core Merger (to implement) ---
class WindowMergeService:
    def __init__(self, kitchen_api: KitchenConfigApiService):
        self.kitchen_api = kitchen_api

    def _mergeSort(self, windows) -> List[Dict]:
        if len(windows) <= 1:
            return windows
        
        mid = len(windows) // 2

        left = self._mergeSort(windows[:mid])
        right = self._mergeSort(windows[mid:])

        return self._mergeAux(left, right)

    def _mergeAux(self, left, right) -> List[Dict]:
        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if (left[i]["start_min"], left[i]["end_min"]) <= (right[j]["start_min"], right[j]["end_min"]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def merge_windows(self, restaurant_id: int) -> List[Dict]:
        """
        Returns:
        List[Dict]: [{"start_min": int, "end_min": int}, ...] consolidated windows sorted by start.
        Notes:
        - Half-open intervals: [start, end)
        - Touching windows merge: next.start <= current_end
        - Ignore invalid windows where end <= start
        """
        # TODO:
        # 1) Fetch windows from API

        resp = None
        retries_n = 3
        delay = 0.1

        for attempt in range(retries_n):
            try:
                resp = self.kitchen_api.get_pickup_windows_for_restaurant(restaurant_id)
            except Exception:
                resp = None

            if resp and resp.status_code == 200:
                break
            if attempt < retries_n - 1:
                time.sleep(delay)
                delay *= 2
            else:
                return []
            
        if resp.windows:
            windows = resp.windows
        else:
            windows = []


        # 2) Filter invalid (end <= start)

        valid = []
        for w in windows:
            if w.end_min > w.start_min:
                valid.append({"start_min": w.start_min, "end_min":  w.end_min})
            
        if not valid:
            return []
        
        # 3) Sort by start_min

        valid = self._mergeSort(valid)

        # 4) Single pass merge using the touching-merge rule
        merged: List[Dict] = []
        current_interval = valid[0]

        for i in range(0, len(valid) - 1):
            start = valid[i + 1]["start_min"]
            end = current_interval["end_min"]
            if start <= end:
                #if valid[i + 1]["end_min"] >= end:
                current_interval = {"start_min": current_interval["start_min"], "end_min": max(valid[i + 1]["end_min"], current_interval["end_min"])}
            else:
                merged.append(current_interval)
                current_interval = valid[i + 1]
        
        merged.append(current_interval)

        # 5) Return consolidated list
        return merged

# --- Test Harness ---
def _print_result(test_name: str, expected, actual):
    status = "PASS" if expected == actual else "FAIL"
    print(f"[{status}] {test_name}")
    print(f" Expected: {expected}")
    print(f" Actual: {actual}\n")
def test_various_shapes():
    windows = [
    PickupWindow( 60, 120), # 1:00-2:00
    PickupWindow(110, 180), # overlaps
    PickupWindow(180, 240), # touches previous end -> merge
    PickupWindow(300, 360), # separate block
    PickupWindow(360, 420), # touches -> merge
    PickupWindow(500, 500), # invalid zero-length -> ignored
    PickupWindow(30, 40), # early short block
    PickupWindow(35, 45), # overlaps early short block
    ]
    mocked_api = KitchenConfigApiService(ListPickupWindowsResponse(windows))
    service = WindowMergeService(mocked_api)
    actual = service.merge_windows(restaurant_id=123)
    expected = [
    {"start_min": 30, "end_min": 45}, # merged early pair
    {"start_min": 60, "end_min": 240}, # merged triple
    {"start_min": 300, "end_min": 420}, # merged touch pair
    ]
    _print_result("Merges overlaps + touching + ignores invalid", expected, actual)

if __name__ == "__main__":
    test_various_shapes()