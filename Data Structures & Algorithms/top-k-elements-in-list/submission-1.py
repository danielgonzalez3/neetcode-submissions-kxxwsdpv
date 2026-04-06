class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        sorted_n = sorted(count, key=lambda x: count[x], reverse=True)
        return sorted_n[:k]