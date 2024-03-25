import re


class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.split(r"\s+", s.strip())[::-1]
        return " ".join(words)


def main() -> None:
    s = "  hello world  "
    solution = Solution()
    result = solution.reverseWords(s)
    print(result)


if __name__ == "__main__":
    main()
