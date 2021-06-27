https://leetcode.com/problems/array-nesting/

# 853 test cases passed out of 856, time limit exceed error

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        def count_elements(nums,curr_element,out_list):
            
            if (curr_element > len(nums)-1) or (nums[curr_element] in out_list):
                return len(out_list)
            
            elif nums[curr_element] not in out_list:
                out_list.append(nums[curr_element])
                curr_element = nums[curr_element]
                out = count_elements(nums, curr_element, out_list)
                return out
        
        total_length_lists = []
        
        for i in range(len(nums)):
            a = count_elements(nums, i, [])
            total_length_lists.append(a)
        
        return max(total_length_lists)
        
        
 
# we can remove total_length_lists which stores the length for each of the element, rather we will just store the max legth

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        def count_elements(nums,curr_element,out_list):
            
            if (curr_element > len(nums)-1) or (nums[curr_element] in out_list):
                return len(out_list)
            
            elif nums[curr_element] not in out_list:
                out_list.append(nums[curr_element])
                curr_element = nums[curr_element]
                out = count_elements(nums, curr_element, out_list)
                return out
        
        max_length = 0
        for i in range(len(nums)):
            a = count_elements(nums, i, [])
            if max_length < a:
                max_length = a
        
        return max_length
        
        
                
            
            
            
            
