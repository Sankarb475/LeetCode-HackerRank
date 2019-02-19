# solution of https://leetcode.com/problems/top-k-frequent-elements/


class TopKFrequentSolution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        nums1 = list(set(nums))
        diction = {}
        for i in nums1:
            diction[i] = 0
        for j in nums:
            diction[j] = diction[j] + 1
        sorted_x = sorted(diction.items(), key=operator.itemgetter(1))[::-1]
        outList = []
        for i in range(k):
            outList.append(sorted_x[i][0]) 
        return outList
            
        
            
            
        
