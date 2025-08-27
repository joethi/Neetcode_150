from typing import Optional, List
import collections
#======================================================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#======================================================================
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            level = []
            len_q = len(q)   
            for i in range(len_q):
                temp = q.popleft()
                level.append(temp.val)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            res.append(level)
        return res
#======================================================================
# Create the tree using TreeNode format
root = TreeNode(
    val=1,
    left=TreeNode(
        val=2,
        left=TreeNode(val=4),
        right=TreeNode(val=5)
    ),
    right=TreeNode(
        val=3,
        left=TreeNode(val=6),
        right=TreeNode(val=7)
    )
)
#======================================================================
sol_obj = Solution()
result = sol_obj.levelOrder(root)
print("result:", result)



