class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)):
            # skip dups we already processed
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # set pointers
            l = i + 1
            r = len(nums) - 1

            while (l < r):
                total = nums[i] + nums[l] + nums[r]
                if (total == 0):
                    sol.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l+=1
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    # move again as there may be more triplets for this i    
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
        return sol