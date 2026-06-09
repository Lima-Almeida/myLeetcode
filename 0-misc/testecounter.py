nums = [1, 2, 1, 3, 1, 2]
freq = {}

for k in nums:
    freq[k] = freq.get(k, 0) + 1

print(freq[1])
