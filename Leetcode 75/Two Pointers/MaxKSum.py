from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1
        return count


def main() -> None:
    nums = [4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4]
    k = 2
    solution = Solution()
    result = solution.maxOperations(nums, k)
    print(result)


if __name__ == "__main__":
    main()
