from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left, right = maxDepth(root.left), maxDepth(root.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        maxDepth(root)
        return self.ans

