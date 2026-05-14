class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char not in map: 
                stack.append(char)
            else:
                if stack:
                    if stack[-1]== map[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return not stack