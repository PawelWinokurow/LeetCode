from typing import Optional, List

from util.tree_node import TreeNode


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answers = []
        self.preorderTraversalUtil(root, answers)
        return answers

    def preorderTraversalUtil(self, root: Optional[TreeNode], answers):
        if root:
            answers.append(root.val)
            self.preorderTraversalUtil(root.left, answers)
            self.preorderTraversalUtil(root.right, answers)