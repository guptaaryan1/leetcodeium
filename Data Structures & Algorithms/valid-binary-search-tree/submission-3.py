# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # if not root or (not root.left and not root.right):
        #     return True
        # if (root.left and root.right):
        #     if (root.left.val >= root.val or root.right.val <= root.val):
        #         return False
        # elif root.left and not root.right:
        #     if root.left.val >= root.val:
        #         return False
        # elif root.right and not root.left:
        #     if root.right.val <= root.val:
        #         return False
        def helper(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)

        return helper(root, float("-inf"), float("inf"))


