class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        for c1, c2 in zip(word1, word2):
            result.append(c1 + c2)
            i += 1
        result.extend(word1[i:] or word2[i:])
        return "".join(result)


def main() -> None:
    s = "abcd"
    t = "pq"
    solution = Solution()
    result = solution.mergeAlternately(s, t)
    print(result)


if __name__ == "__main__":
    main()
