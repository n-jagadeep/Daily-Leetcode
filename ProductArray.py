'''238. Product of Array Except Self
Solved
Medium

Topics
premium lock icon
Companies

Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(1)
        temp = 1
        for i in range(1,len(nums)):
            temp = temp*nums[i-1]
            prefix.append(temp)
        suffix = []
        suffix.append(1)
        temp = 1
        for i in range(len(nums)-2,-1,-1):
            temp = temp*nums[i+1]
            suffix.append(temp)
        suffix = suffix[::-1]
        for i in range(len(nums)):
            nums[i] = (prefix[i]*suffix[i])
        return nums