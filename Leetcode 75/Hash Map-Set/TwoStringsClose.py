from typing import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # freq1 = [0] * 26
        # freq2 = [0] * 26

        # for ch in word1:
        #     freq1[ord(ch) - ord("a")] += 1
        # for ch in word2:
        #     freq2[ord(ch) - ord("a")] += 1
        # for i in range(26):
        #     if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
        #         return False

        # freq1.sort()
        # freq2.sort()
        # return freq1 == freq2

        return (word1_counted := Counter(word1)).keys() == (
            word2_counted := Counter(word2)
        ).keys() and sorted(word1_counted.values()) == sorted(word2_counted.values())


def main() -> None:
    word1 = "abcsaaaaa"
    word2 = "aaabaasac"
    solution = Solution()
    result = solution.closeStrings(word1, word2)
    print(result)


if __name__ == "__main__":
    main()
