#solution of https://leetcode.com/problems/intersection-of-two-arrays/ 

# very fast and memory taking

class IntersectionSolution:
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return list(set(nums1).intersection(nums2))
        
