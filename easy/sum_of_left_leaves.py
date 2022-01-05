from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            sum_l = root.left.val
        else:
            sum_l = self.sumOfLeftLeaves(root.left)
        sum_r = self.sumOfLeftLeaves(root.right)
        return sum_l + sum_r

