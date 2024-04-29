from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] + asteroid < 0:
                        stack.pop()
                    elif stack[-1] + asteroid == 0:
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)
        return stack


def main() -> None:
    asteroids = [8, -8]
    solution = Solution()
    result = solution.asteroidCollision(asteroids)
    print(result)


if __name__ == "__main__":
    main()
