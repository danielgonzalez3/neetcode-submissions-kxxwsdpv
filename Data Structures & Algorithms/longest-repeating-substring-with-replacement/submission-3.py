class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_counts = {}
        max_freq = 0
        left = 0
        longest = 0

        for right in range(len(s)):
            char = s[right]
            
            # expand window
            char_counts[char] = char_counts.get(char, 0) + 1
            max_freq = max(max_freq, char_counts[char])

            # shrink window if too many replacements needed
            while (right - left + 1) - max_freq > k:
                char_counts[s[left]] -= 1
                left += 1

            # update result
            window_size = right - left + 1
            longest = max(longest, window_size)

        return longest