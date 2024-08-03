from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(nums):
    if not nums:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in nums]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            if node.val == val:
                return node
            if node.val > val:
                return dfs(node.left)
            if node.val < val:
                return dfs(node.right)
        return dfs(root)


def main() -> None:
    root_list = [4, 2, 7, 1, 3]
    root = list_to_tree(root_list)
    val = 2

    solution = Solution()
    result = solution.searchBST(root, val)
    print(result)


if __name__ == "__main__":
    main()
