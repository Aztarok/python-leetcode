from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for c in s:
            if c in "({[":
                result.append(c)
            elif c == ")" and len(result) > 0 and result[-1] == "(":
                result.pop()
            elif c == "]" and len(result) > 0 and result[-1] == "[":
                result.pop()
            elif c == "}" and len(result) > 0 and result[-1] == "{":
                result.pop()
            else:
                return False
        return len(result) == 0
        
def main() -> None:
    s = "[[]"
    solution = Solution().isValid(s)
    print(solution)

if __name__ == "__main__":
    main()