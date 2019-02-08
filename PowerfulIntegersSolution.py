# solution of https://leetcode.com/problems/powerful-integers/


#Very fast and memory efficient 

class PowerfulIntegersSolution:
    def powerfulIntegers(self, x: 'int', y: 'int', bound: 'int') -> 'List[int]':
        sumVal = 0
        i = -1
        j = -1
        list1 = []
        sumOut = 0
        if x==1 and y ==1:
            if bound>=2:
                return [2]
            else:
                return []
        if x>1:
            while sumOut <=bound:
                i = i+1
                sumOut = x ** i
        sumOut = 0
        if y >1:
            while sumOut <= bound:
                j = j+1
                sumOut = y **j
        else:
            j = i
            
        if (x<=1):
            i = j
        for m in range(i):
            for n in range(j):
                sumOut = x**m + y ** n
                if (sumOut <= bound):
                    list1.append(sumOut)
                 
        return list(set(sorted(list1)))



class PowerfulIntegersSolution:
    def powerfulIntegers(self, x: 'int', y: 'int', bound: 'int') -> 'List[int]':
        sumVal = 0
        i = -1
        j = -1
        list1 = []
        sumOutX = 0
        sumOutY = 0
        sumOut = 0
        if x==1 and y ==1:
            if bound>=2:
                return [2]
            else:
                return []
        if x>1:
            while sumOutX <=bound:
                i = i+1
                sumOutX = x ** i
        if y >1:
            while sumOutY <= bound:
                j = j+1
                sumOutY = y **j
        else:
            j = i
            
        if (x<=1):
            i = j
        for m in range(i):
            for n in range(j):
                sumOut = x**m + y ** n
                if (sumOut <= bound):
                    list1.append(sumOut)
                 
        return list(set(sorted(list1)))
        


# another solution but slow, would not pass through Leetcode acceptance approval
# time limit exceeded error


class PowerfulIntegersSolution:
    def powerfulIntegers(self, x: 'int', y: 'int', bound: 'int') -> 'List[int]':
        sumVal = 0
        i = -1
        m = True
        n = True
        list1 = []
        while m:
            i = i + 1
            n = True
            j = -1
            if (x**i) > bound:
                m = False
                n = False
            while n:
                j = j + 1
                if (y**j > bound):
                    n= False
                sumVal = x**i + y**j
                if (sumVal <= bound):
                    list1.append(sumVal)
                else:
                    n = False
                sumVal = 0  
        return list(set(sorted(list1)))
                
