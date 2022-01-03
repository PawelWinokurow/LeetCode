from util.tree_node import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            rv, pv, qv = root.val, p.val, q.val
            if rv < min(pv, qv):
                root = root.right
            elif rv > max(pv, qv):
                root = root.left
            else:
                return root




