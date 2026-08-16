# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root1):
            if not root1:
                return 0
            return 1 + max(height(root1.left), height(root1.right))
        res = 0
        if not root:
            return 0
        lh = height(root.left)
        rh = height(root.right)
        d = lh + rh
        ld = self.diameterOfBinaryTree(root.left)
        rd = self.diameterOfBinaryTree(root.right)
        return max(d, ld, rd)
