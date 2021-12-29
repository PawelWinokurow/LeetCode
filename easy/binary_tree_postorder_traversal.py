from typing import Optional, List

from util.tree_node import TreeNode


class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answers = []
        self.postorderTraversalUtil(root, answers)
        return answers

    def postorderTraversalUtil(self, root: Optional[TreeNode], answers):
        if root:
            self.postorderTraversalUtil(root.left, answers)
            self.postorderTraversalUtil(root.right, answers)
            answers.append(root.val)
