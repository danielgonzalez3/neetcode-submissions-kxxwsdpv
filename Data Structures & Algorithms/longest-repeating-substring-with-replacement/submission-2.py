class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_count = 0
        res = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            counts[c] = counts.get(c,0) + 1
            max_count = max(max_count, counts[c])
            while((r-l+1) - max_count) > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res