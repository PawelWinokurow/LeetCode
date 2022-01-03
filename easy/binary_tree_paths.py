from typing import Optional, List

from util.tree_node import TreeNode


class Solution:

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        self.util(root, '', ans)
        return ans

    def util(self, root, s, ans):
        s += str(root.val)
        if root.left:
            self.util(root.left, f'{s}->', ans)
        if root.right:
            self.util(root.right, f'{s}->', ans)
        if not root.left and not root.right:
            ans.append(s)
