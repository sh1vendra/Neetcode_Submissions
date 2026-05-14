class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        maxlen = 0
        for num in setnums:
            if num-1 not in setnums:
                length = 1
                while num+length in setnums:
                    length +=1 
                maxlen = max(maxlen, length)
        return maxlen