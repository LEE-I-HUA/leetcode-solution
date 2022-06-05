# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringDigit=''
        for i in range (len(digits)):
            stringDigit += str(digits[i])
        strNum = str(int(stringDigit)+1)
        result=[]
        for j in range (len(strNum)):
            result.append(int(strNum[j]))
        return result
