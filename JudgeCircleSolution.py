# solution of https://leetcode.com/problems/robot-return-to-origin/        ==> Easy 


class JudgeCircleSolution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        dictionary = {'U':0,'L':0,'R':0,'D':0}
        for i in moves:
            dictionary[i] = dictionary[i] + 1
        if dictionary['U'] - dictionary['D'] == 0 and dictionary['L'] - dictionary['R'] == 0:
            return True
        return False
            
        
