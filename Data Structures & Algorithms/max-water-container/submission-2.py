class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_a = 0
        for i in range(len(heights)):
            l = i
            r = len(heights) - 1
            while(l < r):
                length = r - l
                height = min(heights[r], heights[l])
                max_a = max(length * height, max_a)
                r -= 1
        return max_a
            