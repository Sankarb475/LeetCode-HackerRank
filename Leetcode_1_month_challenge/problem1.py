class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dict1 = {}
        for i in arr:
            if abs(x-i) in dict1:
                dict1[abs(x-i)].append(i)
            else:
                dict1[abs(x-i)] = [i]
    
        out_list = []
        count = 0
        # dict1 = sorted(dict1)
        for key in sorted(dict1.keys()):
            for values in dict1[key]:
                out_list.append(values)
                count = count + 1
                if count == k:
                    return sorted(out_list)

                  
