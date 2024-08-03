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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        maxSum = float("-inf")
        maxLevel = 1
        currentLevel = 1

        while queue:
            sumOfLevel = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sumOfLevel += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sumOfLevel > maxSum:
                maxSum = sumOfLevel
                maxLevel = currentLevel
            currentLevel += 1
        return maxLevel


def main() -> None:
    root_list = [-100, -200, -300, -20, -5, -10, None]
    root = list_to_tree(root_list)

    solution = Solution()
    result = solution.maxLevelSum(root)
    print(result)


if __name__ == "__main__":
    main()
