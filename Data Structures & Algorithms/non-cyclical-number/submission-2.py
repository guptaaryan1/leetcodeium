class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        sq = 0
        while True:
            tmp = 0
            while n > 0:
                tmp += (n % 10) ** 2
                n //= 10
            if tmp in seen:
                return False
            if tmp == 1:
                return True
            seen.add(tmp)

            n = tmp
        return True

        
