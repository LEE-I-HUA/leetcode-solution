# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, 
# it is the product of some integer with itself. For example, 1, 4, 9, 
# and 16 are perfect squares while 3 and 11 are not.

# this solution cannot work cause I ignored the probability that n = ax^2+by^2
class Solution:
    def numSquares(self, n: int) -> int:
        def perfectSquare_1(n):
            count = 0 
            while n > 0:
                # print(math.floor(math.sqrt(n)))
                n = n - (math.floor(math.sqrt(n))**2)
                count = count + 1
            return  count
        def primeFactorization(n):
            a = n
            output=[]
            while n > 1:
                for i in range(2, n+1):
                    if (n % i == 0):
                        n = int(n/i)
                        output.append(i)
                        break
            return(output)

        def perfectSquare_0(list):
            x=1
            for i in list:
                if (list.count(i))%2 != 0:
                    x = x*i
            return(x)
        return min(perfectSquare_1(n),perfectSquare_0(primeFactorization(n)))
