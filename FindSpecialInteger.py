#solution of https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/submissions/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = {}
        # dictionary : keys of which are elements of the array and value is the number of occurence of each element
        for i in arr:
            if i in dic:
                dic[i] = dic[i] + 1
            else:
                dic[i] = 1
        maxKey = max(dic, key=dic.get)
        return maxKey
        
  
        
