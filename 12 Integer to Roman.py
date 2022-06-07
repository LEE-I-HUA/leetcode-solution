# Input: num = 2867
# Output: "MMDCCCLXVII"

class Solution:
    def intToRoman(self, num: int) -> str:
        RomanUnits =['I','IV','V','IX']
        RomanTens = ['X','XL','L','XC']
        RomanHundreds = ['C','CD','D','CM','M']
        ans = ''
        if num % 10 <=3:
            ans=RomanUnits[0]*(num % 10)
        elif num % 10 ==4:
            ans=RomanUnits[1]
        elif num % 10 >=5 and num % 10 < 9:
            ans=RomanUnits[2]+RomanUnits[0]*((num % 10)-5)
        else:
            ans=RomanUnits[3]
        num = num // 10
        
        if num % 10 <=3:
            ans=RomanTens[0]*(num % 10)+ans
        elif num % 10 ==4:
            ans=RomanTens[1]+ans
        elif num % 10 >=5 and num % 10 < 9:
            ans=RomanTens[2]+RomanTens[0]*((num % 10)-5)+ans
        else:
            ans=RomanTens[3]+ans
        num = num // 10    
        
        if num % 10 <=3:
            ans=RomanHundreds[0]*(num % 10)+ans
        elif num % 10 ==4:
            ans=RomanHundreds[1]+ans
        elif num % 10 >=5 and num % 10 < 9:
            ans=RomanHundreds[2]+RomanHundreds[0]*((num % 10)-5)+ans
        else:
            ans=RomanHundreds[3]+ans
        num = num // 10
        
        if num % 10 <=3:
            ans=RomanHundreds[4]*(num % 10)+ans
            
        return ans
