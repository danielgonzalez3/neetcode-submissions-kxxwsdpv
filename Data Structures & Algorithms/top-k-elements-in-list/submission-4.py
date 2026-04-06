from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies
        count = Counter(nums)

        # Step 2: Create buckets
        max_freq = len(nums)
        b = [[] for _ in range(max_freq +1)]
        # Step 3: Fill buckets
        for num, freq in count.items():
            b[freq].append(num)

        # Step 4: Collect top k elements
        result = []
        for freq in range(max_freq, 0, -1):
            if not b[freq]:
                continue

            for num in b[freq]:
                result.append(num)
                if len(result) == k:
                    return result