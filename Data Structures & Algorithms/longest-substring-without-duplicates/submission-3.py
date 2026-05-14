class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        l= 0
        n= len(nums)
        longest = 0
        sett = set()

        for r in range (n):
            while (nums[r] in sett):
                sett.remove(nums[l])
                l += 1
            sett.add(nums[r])
            length = len(sett)
            longest = max(longest, length)
            

        return longest
