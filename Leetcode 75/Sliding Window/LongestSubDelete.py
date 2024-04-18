from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_length = 0
        zero_index = -1
        while right < len(nums):
            curr = nums[right]
            if curr == 0:
                left = zero_index + 1
                zero_index = right
            max_length = max(max_length, right - left)
            right += 1
        return max_length


def main() -> None:
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    solution = Solution()
    result = solution.longestSubarray(nums)
    print(result)


if __name__ == "__main__":
    main()
