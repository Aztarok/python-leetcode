from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        largest = {}
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            if -nums[i] in nums[i + 1:]:
                largest[nums[i]] = -nums[i]
        return (list(largest.values())[-1]) if largest else -1
        

def main():
    nums = [-1,10,6,7,-7,1]
    solution = Solution()
    result = solution.findMaxK(nums)
    print(result)


if __name__ == "__main__":
    main()
