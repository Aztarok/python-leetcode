class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        # New way of doing it which is slower
        # while right < len(t) and left < len(s):
        #     if s[left] == t[right]:
        #         left += 1
        #     right += 1
        # Old solution which is faster
        for right in range(len(t)):
            if s[left] == t[right]:
                left += 1
            if left == len(s):
                return True
        return left == len(s)


def main() -> None:
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    result = solution.isSubsequence(s, t)
    print(result)


if __name__ == "__main__":
    main()
