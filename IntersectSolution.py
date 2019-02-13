# solution of https://leetcode.com/problems/intersection-of-two-arrays-ii/


class IntersectSolution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        listOut = []
        if len(nums1) > len(nums2):
            for a in nums1:
                if a in nums2:
                    nums2.remove(a)
                    listOut.append(a)
        else:
            for a in nums2:
                if a in nums1:
                    nums1.remove(a)
                    listOut.append(a)
            
        return listOut
        
