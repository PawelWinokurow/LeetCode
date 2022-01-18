from typing import Optional

from util.tree_node import TreeNode


class Solution:

    def __init__(self):
        self.mem = {}

    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return abs(self.tree_sum(root.left) - self.tree_sum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)

    def tree_sum(self, root):
        if not root:
            return 0
        if id(root.left) not in self.mem:
            self.mem[id(root.left)] = left = self.tree_sum(root.left)
        if id(root.right) not in self.mem:
            self.mem[id(root.right)] = right = self.tree_sum(root.right)

        return root.val + self.mem[id(root.left)] + self.mem[id(root.right)]
