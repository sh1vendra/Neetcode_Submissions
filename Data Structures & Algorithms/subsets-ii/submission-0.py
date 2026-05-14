class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []
        def backtrack(i, sol):
            if i == len(nums):
                res.append(sol[:])
                return 0
            sol.append(nums[i])
            backtrack(i+1,sol)
            sol.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1,sol)

        backtrack(0,[])
        return res