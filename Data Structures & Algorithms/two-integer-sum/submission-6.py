class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()
        for i, n in enumerate(nums):
            delta = target - n
            if delta in mem:
                return [mem[delta], i]
            else:
                mem[n] = i
        return [-1]