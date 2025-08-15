class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        stack.append(s[0])
        for i in range(1,len(s)):
            #print(i)
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                if not stack or stack[len(stack)-1] == '(' or stack[len(stack)-1] == '{' or stack[len(stack)-1] == '[':
                    stack.append(s[i])
                    #print(stack)
                else:
                    return False
            if s[i] == ')':
                if not stack:
                    return False
                elif stack[len(stack)-1] == '(':
                    stack.pop()
                else:
                    return False
            if s[i] == ']':
                if not stack:
                    return False
                elif stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    return False
            if s[i] == '}':
                if not stack:
                    return False
                elif stack[len(stack)-1] == '{':
                    stack.pop()
                else:
                    return False
        if stack:
            #print(stack)
            return False
        else:
            return True