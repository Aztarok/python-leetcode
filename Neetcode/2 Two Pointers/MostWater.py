from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            left = height[l]
            right = height[r]
            max_area = max(max_area, min(left, right) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area
    
def main() -> None:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result = solution.maxArea(height)
    print(result)

if __name__ == "__main__":
    main()