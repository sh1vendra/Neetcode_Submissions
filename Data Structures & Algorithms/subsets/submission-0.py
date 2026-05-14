class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 'res' will store all the subsets generated.
        # 'sol' is used to build the current subset during the backtracking process.
        res, sol = [], []

        def dfs(i):
            # Base Case: If we've considered all elements,
            # add a copy of the current subset 'sol' to the results.
            if i == len(nums):
                res.append(sol.copy())
                return None
            
            # Decision 1: Include nums[i] in the current subset.
            sol.append(nums[i])
            dfs(i + 1)  # Recurse to the next index with nums[i] included.
            
            # Backtrack: Remove the last element to explore the subset without nums[i].
            sol.pop()
            
            # Decision 2: Exclude nums[i] from the current subset.
            dfs(i + 1)  # Recurse to the next index with nums[i] excluded.

        # Start the recursion from index 0.
        dfs(0)
        # Return the complete list of subsets.
        return res
