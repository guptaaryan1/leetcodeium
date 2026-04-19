class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0 for i in range(len(temperatures))]
        higher = temperatures[-1]
        days = 0
        for i, n in enumerate(temperatures):
            while stk and n > stk[-1][0]:
                stkn, stki = stk.pop()
                res[stki] = (i - stki)
            stk.append([n, i])

        return res