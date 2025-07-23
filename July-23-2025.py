# 1768. Merge Strings Alternately
# Solved
# Easy

# Topics
# premium lock icon
# Companies

# Hint
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 and word2:
            merged = word1[0] + word2[0]
        elif word1:
            return word1
        elif word2:
            return word2
        else:
            return ""
        #print(merged)
        length = max(len(word1),len(word2))
        #print(length)
        for i in range(1,length):
            if (i> len(word1)-1):
                merged = merged + word2[i]
                #print(merged, "inside for", i)
            elif(i> len(word2)-1):
                merged = merged + word1[i]
                #print(merged, "inside elif", i)
            else:
                merged = merged +word1[i] + word2[i]
                #print(merged, "inside else", i)
            #merged = merged + word1[i] + word2[i]
        return merged