# Code

# Testcase
# Testcase

# Test Result
# 345. Reverse Vowels of a String
# Solved
# Easy

# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["A","a","E","e","I","i","O","o","U","u"]
        v = []
        for i in range(len(s)):
            if s[i] in vowels:
                    v.append(s[i])
        
        for i in range(len(s)):
            if s[i] in vowels:
                if i == len(s)-1 :
                    s = s[:i]+v.pop()
                else:
                    s = s[:i]+v.pop()+s[i+1:]

        return s


#two pointer approach

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        i = 0
        j = len(s) -1
        #print("HERE",i,j)
        while(i<j):
            if s[i] not in vowels and s[j] not in vowels:
                i+=1
                j-=1
                #print("if",i,j)
            elif s[i] not in vowels:
                i+=1
                #print("elif1",i,j)
            elif s[j] not in vowels:
                j-=1
                #print("elif2",i,j)
            else:
                s = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                i+=1
                j-=1
                #print("else",i,j,s)
        return s

