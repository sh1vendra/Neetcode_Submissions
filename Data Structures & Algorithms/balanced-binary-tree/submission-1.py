# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(root):
            if not root:
                return 0
            leftH= dfs(root.left)
            rightH= dfs(root.right)
            
            if abs(leftH-rightH) > 1:
                nonlocal ans
                ans = False
                return 0
            return max(leftH,rightH)+1
        dfs(root)
        return ans