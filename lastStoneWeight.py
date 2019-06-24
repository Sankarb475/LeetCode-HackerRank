# solution of https://leetcode.com/problems/last-stone-weight/
# 100% memory effcient

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        flag = True
        while flag:
            stones.sort()
            stones = stones[::-1]
            if len(stones) ==1:
                return stones[0]
            elif len(stones) ==0:
                return 0
            else:
                if stones[0] == stones[1]:
                    stones.pop(0)
                    stones.pop(0)
                elif stones[0] > stones[1]:
                    newVal = stones[0] - stones[1]
                    stones.pop(0)
                    stones[0] = newVal
    
