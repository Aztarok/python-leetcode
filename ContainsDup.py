from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


def main():
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)


if __name__ == "__main__":
    main()
