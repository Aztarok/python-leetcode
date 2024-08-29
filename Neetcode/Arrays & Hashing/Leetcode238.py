from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
        
def main() -> None:
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.productExceptSelf(nums)
    print(result)

if __name__ == "__main__":
    main()