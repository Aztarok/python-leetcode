from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = maxSum = sum(nums[:k])
        for i in range(k, len(nums)):
            currSum = currSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum / k


def main() -> None:
    nums = [-1]
    k = 1
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    print(result)


if __name__ == "__main__":
    main()
