# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
## For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr=str(x)
        reverseX=xStr[::-1]
        if reverseX == xStr:
            return True
        else:
            return False
