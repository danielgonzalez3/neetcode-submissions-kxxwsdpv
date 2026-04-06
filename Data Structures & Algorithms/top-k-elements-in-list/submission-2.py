from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums).most_common(k)
        topK = []
        for x,y in n:
            topK.append(x)
        return topK