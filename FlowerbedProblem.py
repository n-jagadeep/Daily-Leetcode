# FlowerbedProblem.py
# Code

# Testcase

# Test Result
# Test Result
# 605. Can Place Flowers
# Solved
# Easy

# Topics
# premium lock icon
# Companies
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.




class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if i == 0:
                preve = 0
            else:
                preve = flowerbed[i-1]
            if i == len(flowerbed) - 1:
                nexte = 0
            else:
                nexte = flowerbed[i+1]

            if (preve == 0 and nexte == 0 and flowerbed[i]!=1):
                flowerbed[i] = 1
                n-=1
            if n == 0:
                return True
            
        return False
            
