from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        l = 0
        best_l = 0
        best_len = float("inf")

        for r in range(len(s)):
            c = s[r]

            if need[c] > 0:
                missing -= 1

            need[c] -= 1

            while missing == 0:
                if r - l + 1 < best_len:
                    best_l = l
                    best_len = r - l + 1

                need[s[l]] += 1

                if need[s[l]] > 0:
                    missing += 1

                l += 1

        return "" if best_len == float("inf") else s[best_l:best_l + best_len]