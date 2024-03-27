from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)


def main() -> None:
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    result = solution.moveZeroes(nums)
    print(result)


if __name__ == "__main__":
    main()
