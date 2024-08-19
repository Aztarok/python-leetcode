from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        def dfs(node, current):
            return 5
        return dfs(connections[0], 0)


def main() -> None:
    name: str = "Daniel"
    print(name)
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

    solution = Solution()
    result = solution.minReorder(n, connections)
    print(result)


if __name__ == "__main__":
    main()
