class Solution:
    def findMin(self, nums: List[int]) -> int:
        firstIdx = 0
        lastIdx = len(nums) - 1
        
        if(len(nums) == 1):
            return nums[0]

        while(lastIdx - firstIdx >= 2):
            if (nums[(lastIdx + firstIdx) // 2] < nums[lastIdx]):
                lastIdx = (lastIdx + firstIdx) // 2
            else:
                firstIdx = (lastIdx + firstIdx) // 2
        return min(nums[firstIdx], nums[(lastIdx + firstIdx) // 2], nums[lastIdx])


