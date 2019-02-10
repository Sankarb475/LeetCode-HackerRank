#solution of https://leetcode.com/problems/jewels-and-stones/        ==> Easy level

class NumJewelsInStonesSolution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        dictionary = {}
        for i in J:
            dictionary[i] = 0
        for i in S:
            if i in dictionary:
                dictionary[i] =  dictionary[i] + 1
        return sum(dictionary.values())
