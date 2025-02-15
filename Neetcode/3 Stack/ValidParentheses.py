from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in "({[":
                result.append(c)
            elif c in ")}]":
                if not result or result[-1] != mapping[c]:
                    return False
                result.pop()
        return len(result) == 0

        
def main() -> None:
    s = "{([])}"
    solution = Solution().isValid(s)
    print(solution)

if __name__ == "__main__":
    main()