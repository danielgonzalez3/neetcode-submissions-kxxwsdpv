class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1  # Initialize two pointers
        left_max, right_max = height[left], height[right]  # Initialize max heights
        water_trapped = 0  # Initialize result

        while left < right:
            if height[left] < height[right]:
                # Process left side
                if height[left] >= left_max:
                    left_max = height[left]  # Update left_max
                else:
                    water_trapped += left_max - height[left]  # Add trapped water
                left += 1  # Move left pointer to the right
            else:
                # Process right side
                if height[right] >= right_max:
                    right_max = height[right]  # Update right_max
                else:
                    water_trapped += right_max - height[right]  # Add trapped water
                right -= 1  # Move right pointer to the left

        return water_trapped