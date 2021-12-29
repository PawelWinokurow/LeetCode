from typing import Optional

from util.tree_node import TreeNode


class Solution:

    def __init__(self):
        self.d = {}

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if id(root.left) in self.d:
            left = self.d[id(root.left)]
        else:
            left = self.maxDepth(root.left)
            self.d[id(root.left)] = left
        if id(root.right) in self.d:
            right = self.d[id(root.right)]
        else:
            right = self.maxDepth(root.right)
            self.d[id(root.right)] = right
        return 1 + max(left, right)