from typing import List

from util.node import Node


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        ans = []

        while stack:
            root = stack.pop()
            if root:
                ans.append(root.val)
                stack.extend(root.children[::-1])
        return ans
