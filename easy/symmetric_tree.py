from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_symmetric_util(root.left, root.right)

    def is_symmetric_util(self, left, right) -> bool:
        if left and right:
            return left.val == right.val \
                   and self.is_symmetric_util(left.left, right.right) \
                   and self.is_symmetric_util(left.right, right.left)
        return left is right

