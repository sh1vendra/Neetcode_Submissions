# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            
            #Recursive step, we want BOTH of the values True to be True
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)
        def hasSubtree(root):
            if not root:
                return False
            if sameTree(root,subRoot):
                return True
            return hasSubtree(root.left) or hasSubtree(root.right)

        return hasSubtree(root)