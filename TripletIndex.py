

# Code

# Testcase
# Testcase

# Test Result
# 334. Increasing Triplet Subsequence
# Solved
# Medium

# Topics
# premium lock icon
# Companies
# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        for i in nums:
            if i <= min1:
                min1 = i
            elif i <= min2:
                min2 = i
            else:
                return True
        return False


