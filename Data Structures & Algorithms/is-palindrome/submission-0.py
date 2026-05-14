class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr=''
        for n in s:
            if n.isalnum():
                newStr += n.lower()
        return newStr == newStr[::-1]
            
