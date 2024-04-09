class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        if len(s) == 0:
            return True
        for right in range(len(t)):
            if s[left] == t[right]:
                left += 1
            if left == len(s):
                return True
        return False


def main() -> None:
    s = ""
    t = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s, t)
    print(result)


if __name__ == "__main__":
    main()
# 2cb9ff
