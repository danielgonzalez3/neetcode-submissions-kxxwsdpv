class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        max_freq = 0
        longest = 0
        l = 0

        for r in range(len(s)):
            char = s[r]
            
            char_counts[char] = char_counts.get(char, 0 ) + 1
            max_freq = max(max_freq, char_counts[char])

            if ((r - l + 1) - max_freq) > k:
                char_counts[s[l]] -= 1
                l += 1

            window_size = r - l + 1
            longest = max(longest, window_size)

        return longest