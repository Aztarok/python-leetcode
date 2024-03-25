from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        first_min = second_min = float("inf")

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False


def main():
    nums = [20, 100, 10, 12, 5, 13]
    solution = Solution()
    result = solution.increasingTriplet(nums)
    print(result)


if __name__ == "__main__":
    main()
