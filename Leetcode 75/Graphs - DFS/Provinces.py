from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(i: int) -> None:
            visited[i] = True

            for j in range(n):
                if isConnected[i][j] and not visited[j]:
                    dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count


def main() -> None:
    isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    solution = Solution()
    result = solution.findCircleNum(isConnected)
    print(result)


if __name__ == "__main__":
    main()
