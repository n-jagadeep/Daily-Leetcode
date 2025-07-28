# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.




class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        count = 1
        i = 1
        j = len(chars)
        while (i<j):
            #print("i:",i,j)
            #print("chars:",chars)
            if chars[i] == chars[i-1]:
                count +=1
                chars.pop(i)
                j = len(chars)
                #print("ifCount:",count)
            else:
                #print("elseCount:",count)
                if count == 1:
                    i += 1
                    continue
                count = str(count)
                for k in range(len(count)):
                    chars.insert(i+k,count[k])
                    if k == len(count) -1:
                        i+=k
                j = len(chars)
                count = 1
                i+=2
        if count > 1:
            for k in str(count):
                chars.append(k)
        return len(chars)
