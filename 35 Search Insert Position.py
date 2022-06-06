# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return (nums.index(target))
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
