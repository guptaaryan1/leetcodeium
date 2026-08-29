class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        for i in range(len(temperatures) - 1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            if not st:
                res[i] = 0
            else:
                res[i] = st[-1] - i
            st.append(i)
        return res
