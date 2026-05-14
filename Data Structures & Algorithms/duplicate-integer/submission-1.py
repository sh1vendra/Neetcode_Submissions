class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i, value in enumerate(nums):
            if value in d:
                return True
            d[value]=i
        return False