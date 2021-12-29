from typing import Optional, List

from util.tree_node import TreeNode


class Solution:

    def __init__(self):
        self.answer = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorderTraversalUtil(root)
        return self.answer


    def inorderTraversalUtil(self, root):
        if root == None:
            return
        self.inorderTraversalUtil(root.left)
        self.answer.append(root.val)
        self.inorderTraversalUtil(root.right)