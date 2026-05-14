# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def dfs(node):
            if not node:
                return None
            dfs (node.left)
            nonlocal ans
            ans.append(node.val)
            dfs(node.right)
            return ans
        ansList = dfs(root)
        return ansList[k-1]
