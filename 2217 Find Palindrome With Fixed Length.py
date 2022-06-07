# Given an integer array queries and a positive integer intLength, 
# return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.

# A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

# Input: queries = [2,4,6], intLength = 4
# Output: [1111,1331,1551]
# Explanation:
# The first six palindromes of length 4 are:
# 1001, 1111, 1221, 1331, 1441, and 1551.

# 判斷1:queries中的數值是否在intLength = n的回文範圍內
# 判斷2:若是intLength為奇數或偶數?回文範圍內最小的回文如何取得?
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        p1 = '1'
        p1 += '0'*((intLength-1) // 2)
        ans = []
        place = 9*(10**((intLength-1) // 2))
        for i in queries:
            if i <= place:
                strTempt = str(int(p1)+i-1)
                strTempt += strTempt[::-1]
                if (intLength-1) % 2 !=1:
                    strTempt = strTempt[:intLength // 2]+ strTempt[intLength // 2 +1:] 
                ans.append(int(strTempt))
            else:
                ans.append(-1)
            
        return ans
