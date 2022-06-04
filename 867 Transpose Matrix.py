class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        answer=[]
        for i in range (len(matrix[0])):
            tempt=[]
            for j in range (len(matrix)):
                tempt.append(matrix[j][i])
            answer.append(tempt)
        return answer
