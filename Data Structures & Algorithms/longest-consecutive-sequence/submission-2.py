class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # Only start counting if 'n' is the start of a sequence
            if (n - 1) not in numSet:
                current = n
                streak = 1

                # Incrementally check for the next consecutive number
                while (current + 1) in numSet:
                    current += 1
                    streak += 1

                # Update the longest streak found
                longest = max(longest, streak)

        return longest

            