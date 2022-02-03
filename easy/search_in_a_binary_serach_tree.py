from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            elif root.val >= val:
                root = root.left
        return root