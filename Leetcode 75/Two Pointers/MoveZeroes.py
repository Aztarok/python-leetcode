from typing import List


class Solution:
    def moveZeroes(self, nums: list) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] == 0:
                nums[left], nums[right] = nums[right], nums[left]
            if nums[left] != 0:
                left += 1


def main() -> None:
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    result = solution.moveZeroes(nums)
    print(result)


if __name__ == "__main__":
    main()
