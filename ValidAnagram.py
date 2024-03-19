from collections import Counter
from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b = Counter(s)
        c = Counter(t)
        if b == c:
            return True
        else:
            return False


def main() -> None:
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)


if __name__ == "__main__":
    main()
