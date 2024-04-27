from typing import Counter, List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = {}
        count = 0
        for row in grid:
            result[tuple(row)] = result.get(tuple(row), 0) + 1
        for i in range(len(grid[0])):
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            count += result.get(tuple(col), 0)

        return count


def main() -> None:
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    solution = Solution()
    result = solution.equalPairs(grid)
    print(result)


if __name__ == "__main__":
    main()
