from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        
        for n in nums:
            if (n - 1) not in numsSet:
                length = 0
                while (n + length) in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest
        
def main() -> None:
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    solution = Solution().longestConsecutive(nums)
    print(solution)

if __name__ == "__main__":
    main()