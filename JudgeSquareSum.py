# solution of https://leetcode.com/problems/sum-of-square-numbers/

# binary search algo 
class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    result=False
    l=0
    h=math.ceil(math.sqrt(c))    
    while l<=h+1:
        if l*l + h*h==c:
            result=True
            break
        elif l*l + h*h<c:
            l+=1
        else:
            h-=1
    return result


# two pointer solution - fast and efficient
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 1 or c ==0:
            return True
        left = 0
        right = math.ceil(math.sqrt(c))
        while right >= left:
            val = left* left + right*right
            if val == c:
                return True
            elif val > c:
                right = right - 1
            else:
                left = left + 1
        return False


# Time limit exceeds - error - brute force algo

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c ==1 or c==0:
            return True
        for i in range(c):
            if i * i < c:
                for j in range(c):
                    if j * j < c:
                        if i*i + j*j == c:
                            return True
        return False
             
