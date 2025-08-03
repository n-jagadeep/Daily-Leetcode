class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = 'AEIOUaeiou'
        m =0
        arr = s[:k]
        for i in arr:
            if i in v:
                m+=1
        t = m
        for i in range(k,len(s)):
            #print(t,i,k-i)
            if s[i] in v :
                t+=1
            if s[i-k] in v:
                t-=1
            if t >= m:
                m = t
        return m

