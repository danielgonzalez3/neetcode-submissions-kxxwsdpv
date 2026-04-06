class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = []
        m = 0
        for c in s:
            if c in cache:
                m = max(m, len(cache))
                idx = cache.index(c)
                cache = cache[idx + 1:]
            cache.append(c)
        return max(m, len(cache))