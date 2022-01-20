from typing import Optional, List

from util.tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        d = {}
        def util(root, depth):
            if not root:
                return
            d[depth] = d.get(depth, []) + [root.val]
            util(root.left, depth + 1)
            util(root.right, depth + 1)
        util(root, 1)
        return [sum(d[i]) / len(d[i]) for i in sorted(d.keys())]
