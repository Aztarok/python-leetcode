from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        altitude = 0
        for i in gain:
            altitude += i
            max_altitude = max(max_altitude, altitude)
        return max_altitude


def main() -> None:
    gain = [-5, 1, 5, 0, -7]
    solution = Solution()
    result = solution.largestAltitude(gain)
    print(result)


if __name__ == "__main__":
    main()
