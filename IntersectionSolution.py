#solution of https://leetcode.com/problems/intersection-of-two-arrays/ 

# very fast and memory taking

class IntersectionSolution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return list(set(nums1).intersection(nums2))
    
  


class IntersectionSolution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        listOut = []
        if len(nums1) > len(nums2):
            for a in nums2:
                if a in nums1:
                    listOut.append(a)
        else:
            for a in nums1:
                if a in nums2:
                    listOut.append(a)
            
        return list(set(listOut))
        
