from typing import Optional


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
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(node, maxVal):
#             if not node:
#                 return 0
#             res = 1 if node.val >= maxVal else 0
#             maxVal = max(maxVal, node.val)
#             res += dfs(node.left, maxVal)
#             res += dfs(node.right, maxVal)
#             return res
#         return dfs(root, root.val)

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return length

        def dfs(node, length, left):
            if not node:
                return length - 1
            if left:
                return max(dfs(node.left, 1, True), dfs(node.right, length + 1, False))
            else:
                return max(dfs(node.left, length + 1, True), dfs(node.right, 1, False))
        return max(dfs(root.left, 1, True), dfs(root.right, 1, False))


def main() -> None:
    # root_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    # root_list = [3, 1, 4, 3, None, 1, 5]
    root_list = [1, 1, 1, 1, None, None, 1]
    root = list_to_tree(root_list)

    solution = Solution()
    result = solution.longestZigZag(root)
    print(result)


if __name__ == "__main__":
    main()
