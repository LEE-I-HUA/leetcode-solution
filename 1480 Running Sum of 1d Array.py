# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# solution 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer=[]
        sumi = 0
        for i in  nums:
            sumi += i  
            answer.append(sumi)
        return answer
    
# solution 2    
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in range (len(nums)): 
            if i ==0:
                answer.append(nums[i])
            else:
                answer.append(nums[i]+answer[i-1])
        return answer
