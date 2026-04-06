from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        # Function to compute total hours needed to eat all bananas at speed k
        # ????
        def hours_required(k: int) -> int:
            total_hours = 0
            for pile in piles:
                # Using integer math to do ceiling division: ceil(pile / k)
                total_hours += (pile + k - 1) // k
            return total_hours

        # Perform binary search
        while left <= right:
            mid = (left + right) // 2
            if hours_required(mid) <= h:
                # mid is a valid speed, try to see if there's a smaller valid speed
                right = mid - 1
            else:
                # mid is too slow, need to increase speed
                left = mid + 1
        
        # After binary search, 'left' is the smallest speed that meets the requirement
        return left
