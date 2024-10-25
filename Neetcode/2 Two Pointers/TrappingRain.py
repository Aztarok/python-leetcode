from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_rain = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        while l < r:
            print(l_max, r_max)
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                max_rain += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                max_rain += r_max - height[r]
        return max_rain

def main() -> None:
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    solution = Solution()
    result = solution.trap(height)
    print(result)

if __name__ == "__main__":
    main()