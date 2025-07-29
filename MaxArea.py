class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        temp = 0
        i = 0
        j = len(heights)-1
        while(i < j):
            #print(i,j)
            temp = min(heights[i],heights[j]) * (j-i)
            if temp>maxA:
                maxA = temp
            if heights[i]<=heights[j]:
                i+=1
            elif heights[i]>=heights[j]:
                j-=1
            else:
                break
        return maxA