from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.is_equal(root, subRoot) or \
            root.left is not None and self.isSubtree(root.left, subRoot) or \
            root.right is not None and self.isSubtree(root.right, subRoot)

    def is_equal(self, root_1, root_2):
        if not root_1 and root_2 or not root_2 and root_1 or root_1 and root_2 and root_1.val != root_2.val:
            return False
        elif not root_1 and not root_2:
            return True
        else:
            return self.is_equal(root_1.left, root_2.left) and self.is_equal(root_1.right, root_2.right)
