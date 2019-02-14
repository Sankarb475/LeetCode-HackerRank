# solution of https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

#very fast and memory efficient

#implementing two-pointer solution

class TwoSum2Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        i,j = 0, len(numbers)-1
        while i<j:
            if numbers[i] + numbers[j] > target:
                j = j - 1
            elif numbers[i] + numbers[j] < target:
                i = i + 1
            elif numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            
        
