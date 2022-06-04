# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for i in range(1,n+1):
            if i%15 == 0:
                answer.append("FizzBuzz")
                continue
            elif i%5 == 0:
                answer.append("Buzz")
                continue
            elif i%3 == 0:
                answer.append("Fizz")
                continue
            else:
                answer.append(str(i))
                
        return answer
