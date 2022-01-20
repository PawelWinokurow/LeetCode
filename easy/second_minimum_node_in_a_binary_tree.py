from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        values = set()
        arr = [root]

        while arr:
            root = arr.pop()
            values.add(root.val)
            if root.left:
                arr.append(root.left)

            if root.right:
                arr.append(root.right)

        return -1 if len(values) == 1 else list(sorted(values))[1]
