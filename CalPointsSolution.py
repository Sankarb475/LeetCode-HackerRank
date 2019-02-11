#solution of https://leetcode.com/problems/baseball-game/      ==> Easy

# not so memory efficient :P

class CalPointsSolution:
    def calPoints(self, ops: 'List[str]') -> 'int':
        listOut = []
        listSum = 0
        for i in range(len(ops)):
            if self.isInt(ops[i]):
                listOut.append(int(ops[i]))
            elif ops[i] == "C":
                a = listOut.remove(listOut[-1])
                print("a",a)
            elif ops[i] == "D":
                listOut.append(listOut[-1] * 2)
            elif ops[i] == "+":
                listOut.append(listOut[-1] + listOut[-2])
        return sum(listOut)
    
    def isInt(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False
        
        
