class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        transfer = ""
        multiplier = 0

        for char in s:
            if char.isdigit():
                multiplier = multiplier * 10 + int(char)
            elif char == "[":
                stack.append((transfer, multiplier))
                transfer = ""
                multiplier = 0
            elif char == "]":
                prev_transfer, prev_multiplier = stack.pop()
                transfer = prev_transfer + transfer * prev_multiplier
            else:
                transfer += char
        return transfer


def main() -> None:
    s = "100[leetcode]"
    solution = Solution()
    result = solution.decodeString(s)
    print(result)


if __name__ == "__main__":
    main()
