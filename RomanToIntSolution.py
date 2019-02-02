#solution of https://leetcode.com/problems/roman-to-integer/

class RomanToIntSolution:
    def romanToInt(self, s):
        inputList = list(s)
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        outputNum = 0
        bool = False
        if(len(s) == 1):
            outputNum = outputNum + romanDict[s]
        for i in range(len(inputList) -1):
            if (bool) :
                bool = False
                continue
            if romanDict[inputList[i]] > romanDict[inputList[i + 1]]:
                outputNum = outputNum + romanDict[inputList[i]]
                if(i == len(inputList) - 2):
                    outputNum = outputNum + romanDict[inputList[i+1]]
            elif romanDict[inputList[i]] == romanDict[inputList[i + 1]]:
                outputNum = outputNum + romanDict[inputList[i]]
                if(i == len(inputList)-2):
                    outputNum = outputNum + romanDict[inputList[i + 1]]
            else:
                outputNum = outputNum + romanDict[inputList[i + 1]] - romanDict[inputList[i]]
                if (i + 3 == len(inputList)):
                    outputNum = outputNum + romanDict[inputList[i + 2]]
                bool = True

        return outputNum

