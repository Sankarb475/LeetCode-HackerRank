# solution of https://leetcode.com/problems/longest-common-prefix/

class LongestCommonPrefixSolution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(set(strs)) ==1):
            return strs[0]
        if(len(strs) == 0):
            return ""
        if(len(strs) ==1):
            return strs[0]
        list = []
        list1 = []
        for i in strs:
            list.append(len(i))
        size = min(list)
        if (size == 0):
            return ""
        for j in range(size+1):
            for a in strs:
                list1.append(a[:j+1])
            set1 = set(list1)
            if(len(set1) == 1):
                list1 = []
            else:
                return a[:j]
        
        
            
            
        
