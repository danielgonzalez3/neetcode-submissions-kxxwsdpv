class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = [1] * len(nums)
        r_prod = [1] * len(nums)
        size = len(nums) - 1
        for l in range(size):
            l_prod[l + 1] = l_prod[l] * nums[l]
        for r in range(size):
            r_prod[size - r - 1] = r_prod[size - r] * nums[size - r]
            l_prod[size - r - 1] *= r_prod[size - r - 1]
        return l_prod
        # 1 1 2 8 
        # 48 24 6 1
        