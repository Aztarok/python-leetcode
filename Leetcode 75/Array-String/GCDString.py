class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b
        return str1[:a]


def main() -> None:
    s = "ABABABAB"
    t = "ABAB"
    solution = Solution()
    result = solution.gcdOfStrings(s, t)
    print(result)


if __name__ == "__main__":
    main()
