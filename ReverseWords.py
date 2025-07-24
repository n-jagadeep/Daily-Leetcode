# Code

# Testcase
# Testcase

# Test Result
# 151. Reverse Words in a String
# Solved
# Medium

# Topics
# premium lock icon
# Companies
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        #print (words)
        result = ""
        temp = []
        for i in words:
            if i == "":
                continue
            else:
                temp.append(i)
        for i in range(len(temp)-1, -1,-1):
            if i == 0:
                result = result = result +(temp[i])
            else:
                result = result +(temp[i])+ " "
            #print(result)
        #print(result)
        return result