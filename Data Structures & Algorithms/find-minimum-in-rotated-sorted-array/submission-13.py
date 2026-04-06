class Solution:
    def findMin(self, nums: List[int]) -> int:
        end_idx = len(nums)-1
        mid_idx = (end_idx)//2

        search_start = 0
        search_end = mid_idx
        val = nums[0]

        if (nums[mid_idx] > nums[end_idx]):
            search_start = mid_idx
            search_end = end_idx
        
        print(search_start, search_end)

        for n in nums[search_start:search_end+1]:
            print(n)
            val = min(val, n)

        return val
        
