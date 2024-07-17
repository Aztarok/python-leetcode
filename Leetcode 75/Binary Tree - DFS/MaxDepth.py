from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        print(self.val)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return 1 + self.maxDepth(root.right)
        if root.right is None:
            return 1 + self.maxDepth(root.left)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main() -> None:
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    result = solution.maxDepth(root)
    print("Max Depth:", result)


if __name__ == "__main__":
    main()
