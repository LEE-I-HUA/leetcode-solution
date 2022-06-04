# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# should drop the space in list. 
# str.strip([chars]), [chars] is the element need to be drop.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.split(" ")
        tempt = []
        for ele in x:
            if ele.strip():
                tempt.append(ele)

        return len(tempt[-1])
