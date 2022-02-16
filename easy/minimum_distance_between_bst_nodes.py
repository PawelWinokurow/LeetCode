from typing import Optional

from util.tree_node import TreeNode


class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def fn(node, lo, hi):
            if not node:
                return hi - lo
            left = fn(node.left, lo, node.val)
            right = fn(node.right, node.val, hi)
            return min(left, right)
        return fn(root, float('-inf'), float('inf'))
