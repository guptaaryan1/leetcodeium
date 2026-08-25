class MinStack:

    def __init__(self):
        self.st = []
        self.mst = []

    def push(self, val: int) -> None:
        if self.st:

            self.st.append(val)
            self.mst.append(min(self.mst[-1], val))
        else:
            self.st.append(val)
            self.mst.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.mst.pop()
        

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        
        return self.mst[-1]