class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            tmp_count = 1
            delta = 1
            while (n-delta) in numSet:
                tmp_count += 1
                delta += 1
            longest = max (longest, tmp_count)
        return longest
            