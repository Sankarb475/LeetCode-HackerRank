# solution of https://leetcode.com/problems/set-mismatch/         ==> Easy level


class FindErrorNumsSolution:
    def findErrorNums(self, nums: 'List[int]') -> 'List[int]':
        listOut = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                listOut.append(nums[i])
        a = list(set(nums))
        if len(a) == 1 and a[0] ==1:
            listOut.append(2)
            return listOut
        if len(a) == 1 and a[0] ==2:
            listOut.append(1)
            return listOut
        for i in range(len(a)-1):
            if a[0] != 1:
                listOut.append(1)
                break
            elif a[i] + 1 != a[i+1]:
                listOut.append(a[i] + 1)
                break
        if len(listOut) == 1:
            listOut.append(nums[-1] + 1)
        return listOut
            

#another way of soving it

class FindErrorNumsSolution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        s = set([])
        
        total = 0
        target = 0
        dupe = None
        
        for i in range(1, len(nums)+1):
            target += i
            this = nums.pop()
            
            if this in s:
                dupe = this
            else:
                s.add(this)
                total += this
                
        
        return [dupe, target-total]
            
