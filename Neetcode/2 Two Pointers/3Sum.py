from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum > 0:
                   right -= 1 
                elif sum < 0:
                    left +=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

def main() -> None:
    nums = [-2,0,0,2,2]
    solution = Solution().threeSum(nums)
    print(solution)

if __name__ == "__main__":
    main()