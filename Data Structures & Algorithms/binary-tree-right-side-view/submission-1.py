# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            level = []
            qLen = len(q)
            for i in range(qLen):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if level:
                res.append(level[-1])
        return res
