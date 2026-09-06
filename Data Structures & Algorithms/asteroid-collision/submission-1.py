class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        i = 0

        while i < len(asteroids):
            if not st or st[-1] < 0 or asteroids[i] > 0:
                st.append(asteroids[i])
                i += 1
                continue

            alive = True

            while st and st[-1] > 0 and asteroids[i] < 0:
                if abs(st[-1]) < abs(asteroids[i]):
                    st.pop()
                elif abs(st[-1]) == abs(asteroids[i]):
                    st.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break

            if alive:
                st.append(asteroids[i])

            i += 1

        return st


