import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we need at least 'size' hours to eat all the bananas.
        # inf high hourly rate to have size hours of bananas.
        # h / sz
        # bananas/h
        # totalbananas/totalh
        l = 1 
        r = max(piles)
        mink = r
        while l <= r:
            mid = (r + l) // 2
            hours = 0
            for some in piles:
                hours += math.ceil(some / mid)
            if (hours <= h):
                mink = min(mink, mid)
                r = mid - 1
            else:
                l = mid + 1
        return mink

            


        
