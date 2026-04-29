class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in n_set:
                length = 1
                current = n
                while(current + 1 in n_set):
                    length += 1
                    current += 1
                longest = max(length, longest)
        return longest