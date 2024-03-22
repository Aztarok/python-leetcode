from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if (
                flowerbed[i] == 0
                and (i == 0 or flowerbed[i - 1] == 0)
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            ):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


def main() -> None:
    s = [1, 0, 0, 0, 0, 1]
    t = 1
    solution = Solution()
    result = solution.canPlaceFlowers(s, t)
    print(result)


if __name__ == "__main__":
    main()
