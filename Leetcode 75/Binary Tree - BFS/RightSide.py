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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.left = []
        self.right = []

        def bfs(node):
            if not node:
                return
            queue = deque([node])
            while queue:
                length = len(queue)
                for i in range(length):
                    node = queue.popleft()
                    if i == length - 1:
                        self.right.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        bfs(root)
        return self.right


def main() -> None:
    root_list = [1, 2, 3, None, 5, None, 5, 45]
    root = list_to_tree(root_list)

    solution = Solution()
    result = solution.rightSideView(root)
    print(result)


if __name__ == "__main__":
    main()
