# solution of =>  https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        start = '1'
        output = ''
        num = []
        for j in range(1,n):
            for i in range(len(start)):
                if len(num)==0 or start[i] in num:
                    num.append(start[i])
                else:
                    output = output + str(len(num)) + str(num[0])
                    num = []
                    num.append(start[i])
            start = output + str(len(num)) + str(num[0])
            output = ''
            num = []
        return start 
        
        
