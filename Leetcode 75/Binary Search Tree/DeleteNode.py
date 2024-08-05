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


# class Solution:
#     def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
#         def dfs(node):
#             if not node:
#                 return None
#             if node.val == val:
#                 return node
#             if node.val > val:
#                 return dfs(node.left)
#             if node.val < val:
#                 return dfs(node.right)
#         return dfs(root)

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return node
            if key < node.val:
                node.left = self.deleteNode(node.left, key)
            elif key > node.val:
                node.right = self.deleteNode(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                temp = node.right
                while temp.left:
                    temp = temp.left
                node.val = temp.val
                node.right = self.deleteNode(node.right, temp.val)
            return node
        return dfs(root, key)


def main() -> None:
    root_list = [5, 3, 6, 2, 4, None, 7]
    root = list_to_tree(root_list)
    key = 3

    solution = Solution()
    result = solution.deleteNode(root, key)
    print(result)


if __name__ == "__main__":
    main()
