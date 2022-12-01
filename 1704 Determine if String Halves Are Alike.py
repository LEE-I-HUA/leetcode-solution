class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s1 = 0
        for i in range(0, len(s)):
            if i < len(s)/2:
                if s[i] in vowel:
                    s1 += 1
            else:
                if s[i] in vowel:
                    s1 -= 1
        if s1 == 0: return True
