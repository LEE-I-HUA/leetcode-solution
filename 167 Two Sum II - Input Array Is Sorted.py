# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.


# this solution couldn't work because of Time Limit Exceeded
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        tempt = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                tempt.append(numbers[i]+numbers[j])
                if target in tempt:
                    i += 1
                    j += 1
                    return [i,j]
                 
# binary search solution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers)-1
        left,right = 0,r
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1
