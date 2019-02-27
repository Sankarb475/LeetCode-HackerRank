# solution of https://leetcode.com/problems/add-to-array-form-of-integer/ ==> easy


#fast and memory efficient

class AddToArrayFormSolution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        b = ''.join(list(map(str,A)))
        c = list(str(int(b) + K))
        return list(map(int,c))


#another way of solving it

class AddToArrayFormSolution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
	    ret = []

	    while len(A) or K:
		    if len(A): K += A.pop(-1)
		    ret.append(K % 10)
		    K //= 10

	    return ret[::-1]
