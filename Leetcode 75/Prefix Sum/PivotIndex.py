from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num
        return -1


def main() -> None:
    nums = [2, 1, -1]
    solution = Solution()
    result = solution.pivotIndex(nums)
    print(result)


if __name__ == "__main__":
    main()
