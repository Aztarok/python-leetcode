class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        left = 0
        max_vowels = 0
        current_vowels = 0
        for right in range(len(s)):
            if s[right] in vowels:
                current_vowels += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    current_vowels -= 1
                left += 1
            max_vowels = max(max_vowels, current_vowels)
        return max_vowels


def main() -> None:
    s = "abciiidef"
    k = 3
    solution = Solution()
    result = solution.maxVowels(s, k)
    print(result)


if __name__ == "__main__":
    main()
