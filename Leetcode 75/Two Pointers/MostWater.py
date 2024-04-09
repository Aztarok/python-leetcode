from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


def main() -> None:
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    result = solution.maxArea(height)
    print(result)


if __name__ == "__main__":
    main()
