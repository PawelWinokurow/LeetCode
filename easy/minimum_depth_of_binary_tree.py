from typing import Optional

from util.tree_node import TreeNode


class Solution:

    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return 1 + (min(left, right) or max(left, right))
