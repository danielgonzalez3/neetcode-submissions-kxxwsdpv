class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = dict()
        for s in strs:
            sorted_s = tuple(sorted(s))
            if sorted_s in cache:
                cache[sorted_s].append(s)
            else:
                cache[sorted_s] = [s]
        return list(cache.values())