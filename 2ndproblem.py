# 1071. Greatest Common Divisor of Strings
# Solved
# Easy

# Topics
# premium lock icon
# Companies

# Hint
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            #print("going first if")
            return ""
        if str1 == str2:
            #print("going first 2 if")
            return str1
        elif(len(str1) == len(str2)):
            #print("going first 3 if")
            return ""
        if (len(str1)>len(str2)):
            #print("going first 4 if")
            smallest = str2
            smal = len(str2)
        else:
            #print("going first 5 if")
            smallest = str1
            smal = len(str1)
        for i in range(smal):
            #print(smal,i, smallest)
            if(len(str2)%smal != 0):
                #print("GOING IF", len(str2), smal)
                smal = smal - 1
                continue
            if(len(str1)%smal != 0):
                #print("GOING ELSE", len(str2), smal)
                smal = smal - 1
                continue
            result = smallest[0:smal]
            #print(result)
            #print(smal,i, smallest, result)
            div1 = int(len(str1)/smal)
            div2 = int(len(str2)/smal)
            if (div1*result == str1) and (div2*result == str2):
                return result
            smal = smal - 1
        return ""