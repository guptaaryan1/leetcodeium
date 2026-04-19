class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in range(len(tokens)):
            if ((tokens[i][0] == '-' and len(tokens[i]) > 1) or tokens[i].isnumeric()):
                stk.append(int(tokens[i]))
            else:
                if stk:
                    print(stk)
                    n1 = stk.pop()
                    n2 = stk.pop()
                    if (tokens[i] == '+'):
                        stk.append(n1 + n2)
                    elif (tokens[i] == '-'):
                        stk.append(n2 - n1)
                    elif (tokens[i] == '/'):
                        print(f'{n2} / {n1}')
                        stk.append(int(n2/n1))
                    elif tokens[i] == '*':
                        stk.append(n1 * n2)
        return stk[0]
                