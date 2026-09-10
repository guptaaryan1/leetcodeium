class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        for i in range(2, n + 1):
            one, two = two, one + two
        return one



