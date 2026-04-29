from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        m = len(nums)
        b = [[] for _ in range(m+1)]
        for num, freq in count.items():
            b[freq].append(num)
        
        res = []
        for i in range(m, 0, -1):
            if not b[i]:
                continue
            for n in b[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return [-1]