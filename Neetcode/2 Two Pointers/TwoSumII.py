from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
                
        return [left, right]
        
def main() -> None:
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution().twoSum(numbers, target)
    print(solution)

if __name__ == "__main__":
    main()