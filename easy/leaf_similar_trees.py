from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafs_1 = []
        leafs_2 = []
        def traverse(root, leafs):
            if not root:
                return
            if not root.left and not root.right:
                leafs.append(root.val)
            traverse(root.left, leafs)
            traverse(root.right, leafs)
        traverse(root1, leafs_1)
        traverse(root2, leafs_2)
        return leafs_1 == leafs_2
