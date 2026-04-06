class Solution:
    def findMin(self, nums: List[int]) -> int:
        start_idx = 0
        end_idx = len(nums)-1

        def splitMinList(start_idx, end_idx):
            if (start_idx+1 == end_idx or start_idx == end_idx):
                return min(nums[start_idx], nums[end_idx])
            mid_idx = (start_idx + end_idx) // 2
            if (nums[mid_idx] > nums[end_idx]):
                start_idx = mid_idx
                mid_idx = end_idx
            return splitMinList(start_idx, mid_idx)

        return splitMinList(start_idx, end_idx)
        
