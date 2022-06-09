# Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. 
# If it is impossible for b to be a substring of a after repeating it, return -1.

# Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".
## a may longer than b sometimes

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        ans = b.count(a)
        bTest = b.count(a)*a
        if bTest == b:
            ans = b.count(a)
        elif (a + bTest).count(b) == 1:
            ans += 1
        elif (bTest + a).count(b) == 1:
            ans += 1    
        elif (a + bTest + a).count(b) == 1:
            ans += 2
        elif len(a) > len(b):
            if a.count(b) != 0:
                ans = 1
            else:
                ans = -1
        else:
            ans = -1
        return ans
