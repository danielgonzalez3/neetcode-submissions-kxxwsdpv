from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            # Debug statements to trace the values
            print(f"Checking indices ({left}, {right}) with values ({numbers[left]}, {numbers[right]})")
            print(f"Current sum: {current_sum}, Target: {target}")
            
            if current_sum == target:
                # Found the solution; return 1-based indices
                print(f"Found target sum at indices {left + 1} and {right + 1}")
                return [left + 1, right + 1]
            elif current_sum < target:
                # Need a larger sum; move the left pointer to the right
                print("Current sum is less than target. Moving left pointer to the right.")
                left += 1
            else:
                # Need a smaller sum; move the right pointer to the left
                print("Current sum is greater than target. Moving right pointer to the left.")
                right -= 1
        
        # If no solution is found, though the problem states there is one
        print("No two sum solution exists.")
        return []
