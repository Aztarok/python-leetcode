from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        newS = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if newS[left] in vowels and newS[right] in vowels:
                newS[left], newS[right] = newS[right], newS[left]
                left += 1
                right -= 1
            elif newS[left] in vowels:
                right -= 1
            else:
                left += 1
        return "".join(newS)


def main() -> None:
    s = "leetcode"
    solution = Solution()
    result = solution.reverseVowels(s)
    print(result)


if __name__ == "__main__":
    main()
