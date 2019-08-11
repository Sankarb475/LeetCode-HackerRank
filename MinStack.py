# solution of https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []

    def push(self, x: int) -> None:
        self.__stack.append(x)

    def pop(self) -> None:
        self.__stack.pop()
    
    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return min(self.__stack)
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
