from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root_ip = TreeNode()

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
# Create the nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Pass the root to the invertTree function
solution = Solution()
inverted_root = solution.invertTree(root)    
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         while len(root):
                
#         return 0