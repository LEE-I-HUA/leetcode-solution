# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Input: x = 120
# Output: 21
# Input: x = -123
# Output: -321

class Solution:
    def reverse(self, x: int) -> int:
        def split(string):
            return [char for char in string]
        def reversePaste(list):
            s = ''
            for i in list:
                s = i+s
            return s
        
        xString = split(str(abs(x))) # change string to list
        if xString[-1] == 0:
            xString = xString.pop() 
        # reverse the list and change type as string than change type to integer
        ans = int(reversePaste(xString))    
        if x < 0 and ans < 2**(31):
            return -ans
        if x > 0 and ans < 2**(31)-1:
            return ans
        else:
            return 0
