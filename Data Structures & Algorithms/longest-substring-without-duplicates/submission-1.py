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
            length = len(sett)+1
            longest = max(longest, length)
            sett.add(nums[r])

        return longest
