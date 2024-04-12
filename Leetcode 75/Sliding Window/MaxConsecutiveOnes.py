from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count = 0
        zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            count = max(count, right - left + 1)

        return count


def main() -> None:
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    solution = Solution()
    result = solution.longestOnes(nums, k)
    print(result)


if __name__ == "__main__":
    main()
