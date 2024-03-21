from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            check = 0
            current = flowerbed[i]
            if current == 0:
                check = check + 1
        if check % 2 == 0:
            return True
        else:
            return False


def main() -> None:
    s = [1, 0, 0, 0, 1]
    t = 1
    solution = Solution()
    result = solution.canPlaceFlowers(s, t)
    print(result)


if __name__ == "__main__":
    main()
