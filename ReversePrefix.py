class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i + 1][::-1] + word[i+1:]
        return word

def main():
    word = "abcdefd"
    ch = "d"
    solution = Solution()
    result = solution.reversePrefix(word, ch)
    print(result)


if __name__ == "__main__":
    main()
