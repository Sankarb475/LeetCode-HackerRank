# solution of https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        addList = address.split('.')
        output = ''
        for i in addList:
            output = output + "[.]" + i
        return output[3:]
        
 
