from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        print(self.val)


class Solution:
    def __init__(self):
        self.store1 = []
        self.store2 = []

    def collectLeaves(self, node: Optional[TreeNode], store: list):
        if node is None:
            return
        if node.left is None and node.right is None:
            store.append(node.val)
        else:
            self.collectLeaves(node.left, store)
            self.collectLeaves(node.right, store)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.collectLeaves(root1, self.store1)
        self.collectLeaves(root2, self.store2)
        return self.store1 == self.store2


def main() -> None:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(8)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(7)
    root2.left.right.right = TreeNode(4)
    root2.right = TreeNode(1)
    root2.right.left = TreeNode(9)
    root2.right.right = TreeNode(8)

    solution = Solution()
    result = solution.leafSimilar(root1=root, root2=root2)
    print(result)


if __name__ == "__main__":
    main()
