from typing import Optional

from util.tree_node import TreeNode


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ''
        left_str = f'({self.tree2str(root.left)})' if root.left or root.right else f''
        right_str = f'({self.tree2str(root.right)})' if root.right else f''
        return f'{root.val}{left_str}{right_str}'