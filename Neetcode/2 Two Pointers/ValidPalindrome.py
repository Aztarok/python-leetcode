import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        print(s)
        left, right = 0, len(s) - 1
        for left in range(len(s) // 2):
            if s[left] != s[right]:
                return False
            right -= 1
        return True
    
def main() -> None:
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)

if __name__ == "__main__":
    main()