from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def PrintTree(self):
        print(self.val)


# class Solution:
#     # def __init__(self):
#     #     self.paths = []
#     #     self.numPaths = 0
#     #     self.currentNums = 0

#     # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#     #     if root is None:
#     #         return 0
#     #     if root.left is None and root.right is None:
#     #         self.currentNums += root.val
#     #         if self.currentNums == targetSum:
#     #             self.numPaths += 1
#     #         return
#     #     else:
#     #         self.paths.append(root.val)
#     #         if root.left is not None:
#     #             self.currentNums += root.val
#     #             if self.currentNums >= targetSum:
#     #                 self.currentNums -= root.val
#     #             else:
#     #                 self.currentNums = root.val
#     #                 self.numPaths += 1
#     #             self.pathSum(root.left, targetSum)
#     #         if root.right is not None:
#     #             self.currentNums += root.val
#     #             if self.currentNums >= targetSum:
#     #                 self.currentNums -= root.val
#     #             else:
#     #                 self.currentNums = root.val
#     #             self.pathSum(root.right, targetSum)
#     #     return self.numPaths
#     def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         if root is None:
#             return 0
#         return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

#     def dfs(self, node: Optional[TreeNode], targetSum: int) -> int:
#         if node is None:
#             return 0
#         count = 0
#         if node.val == targetSum:
#             count += 1
#         count += self.dfs(node.left, targetSum - node.val)
#         count += self.dfs(node.right, targetSum - node.val)
#         return count

class Solution:
    def __init__(self):
        self.prefix_sum_count = {0: 1}
        self.num_paths = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.dfs(root, 0, targetSum)
        return self.num_paths

    def dfs(self, node: Optional[TreeNode], current_sum: int, targetSum: int) -> None:
        if node is None:
            return

        current_sum += node.val

        if (current_sum - targetSum) in self.prefix_sum_count:
            self.num_paths += self.prefix_sum_count[current_sum - targetSum]

        self.prefix_sum_count[current_sum] = self.prefix_sum_count.get(
            current_sum, 0) + 1

        self.dfs(node.left, current_sum, targetSum)
        self.dfs(node.right, current_sum, targetSum)

        self.prefix_sum_count[current_sum] -= 1  # Backtrack


def main() -> None:
    # root = TreeNode(10)
    # root.left = TreeNode(5)
    # root.left.left = TreeNode(3)
    # root.left.left.left = TreeNode(3)
    # root.left.left.right = TreeNode(-2)
    # root.left.right = TreeNode(2)
    # root.left.right.right = TreeNode(1)
    # root.right = TreeNode(-3)
    # root.right.right = TreeNode(11)
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    solution = Solution()
    targetSum = 22
    result = solution.pathSum(root, targetSum)
    print(result)


if __name__ == "__main__":
    main()
