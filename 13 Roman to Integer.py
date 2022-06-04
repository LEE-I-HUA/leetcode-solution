# I=1, V=5, X=10, L=50, C=100, D=500, M=1000
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        value = [1, 5, 10, 50, 100, 500, 1000]
        lst = []
        for w in s:
            lst.append(w)
            
        answer = 0
        for i in range(len(lst)):
            answer += value[symbol.index(lst[i])]
            if i == len(lst)-1 and lst[i] == 'C':
                break
            elif lst[i]== "C" and (lst[i+1]== "M" or lst[i+1] == "D"):
                answer -= 200
            if i == len(lst)-1 and lst[i] == 'X':
                break
            elif lst[i] == 'X' and (lst[i+1] == 'L' or lst[i+1] == 'C'):
                answer -= 20
            if i == len(lst)-1 and lst[i] == 'I':
                break
            elif lst[i] == 'I' and (lst[i+1] == 'V' or lst[i+1] == 'X'):
                answer -= 2
        return answer
