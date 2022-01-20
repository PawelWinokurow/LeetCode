from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        ans = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        ans.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        ans.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)
        return ans