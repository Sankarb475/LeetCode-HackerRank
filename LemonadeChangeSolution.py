# solution of https://leetcode.com/problems/lemonade-change/


class LemonadeChangeSolution:
    def lemonadeChange(self, bills: 'List[int]') -> 'bool':
        balance = {5:0,10:0,20:0}
        for i in bills:
            if i == 5:
                balance[5] = balance[5] + 1
                continue
            elif i == 10:
                if balance[5] >0:
                    balance[5] = balance[5] - 1
                    balance[10] = balance[10] + 1
                else:
                    return False
            elif i == 20:
                if balance[10] >= 1 and balance[5] >=1:
                    balance[5] = balance[5] - 1
                    balance[10] = balance[10] - 1
                    balance[20] = balance[20] + 1
                elif balance[5] >=3:
                    balance[5] = balance[5] - 3
                    balance[20] = balance[20] + 1
                else:
                    return False
        return True
    
    
