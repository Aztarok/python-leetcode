class Solution:
    # Attempt 1
    # def removeStars(self, s: str) -> str:
    #     new_s = ""
    #     skip_next = False
    #     for i, char in enumerate(s):
    #         if char == "*":
    #             if i > 0:
    #                 new_s = new_s[:-1]
    #                 continue
    #         else:
    #             new_s += char
    #     return new_s

    # Attempt 2
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


def main() -> None:
    s = "leet**co*d*e"
    solution = Solution()
    result = solution.removeStars(s)
    print(result)


if __name__ == "__main__":
    main()
