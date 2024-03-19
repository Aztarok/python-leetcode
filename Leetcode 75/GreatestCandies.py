from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= maxCandy)
        return result


def main() -> None:
    s = [2, 5, 5, 9, 2, 7, 1, 3, 4]
    t = 5
    solution = Solution()
    result = solution.kidsWithCandies(s, t)
    print(result)


if __name__ == "__main__":
    main()
