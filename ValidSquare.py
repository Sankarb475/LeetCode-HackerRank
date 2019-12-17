# solution of https://leetcode.com/problems/valid-square

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        list1 = [p1,p2,p3,p4]
        list1.sort()
        dedup = [list1[i] for i in range(len(list1)) if i == 0 or list1[i] != list1[i-1]]
        if len(dedup) !=4:
            return False
        p1 = list1[0]
        p2 = list1[1]
        p3 = list1[2]
        p4 = list1[3]
        p1p2 = math.sqrt((p2[1]-p1[1])**2 + (p2[0] - p1[0])**2)
        p1p3 = math.sqrt((p3[1]-p1[1])**2 + (p3[0] - p1[0])**2)
        p2p4 = math.sqrt((p4[1]-p2[1])**2 + (p4[0] - p2[0])**2)
        p3p4 = math.sqrt((p4[1]-p3[1])**2 + (p4[0] - p3[0])**2)
        p1p4 = math.sqrt((p4[1]-p1[1])**2 + (p4[0] - p1[0])**2)
        p2p3 = math.sqrt((p3[1]-p2[1])**2 + (p3[0] - p2[0])**2)
        if p1p2 == p3p4 == p1p3 == p2p4 and p1p4==p2p3:
            return True
        return False
        
