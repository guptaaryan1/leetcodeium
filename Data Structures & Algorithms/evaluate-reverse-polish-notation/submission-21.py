class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for tok in tokens:
            if tok == '/':
                b = st.pop()
                a = st.pop()
                st.append(int(a / b))
            elif tok == "+":
                b = st.pop()
                a = st.pop()
                st.append(a + b)
            elif tok == "-":
                b = st.pop()
                a = st.pop()
                st.append(a - b)
            elif tok == "*":
                b = st.pop()
                a = st.pop()
                st.append(a * b)
            else:
                st.append(int(tok))
        return st[0]