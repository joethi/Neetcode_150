from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        cur = root
        while cur or stack:
            while cur.left:
                stack.append(cur.left)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
# Create the tree using TreeNode format
root = TreeNode(
    val=4,
    left=TreeNode(
        val=3,
        left=TreeNode(val=2)
    ),
    right=TreeNode(
        val=5
    )
)
# root=[2,1,3]
k = 4
#======================================================================
sol_obj = Solution()
result = sol_obj.kthSmallest(root, k)
print("result:", result)



