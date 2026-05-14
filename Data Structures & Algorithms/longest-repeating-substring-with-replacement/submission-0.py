class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, longest = 0, 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0) + 1
            windowlen = i-l+1
            if windowlen - max(count.values()) <= k:
                longest = max(longest,windowlen)
            else: 
                count[s[l]] -= 1
                l += 1
        return longest
