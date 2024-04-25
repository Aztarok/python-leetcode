from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        list_set = {}
        for i in arr:
            if i in list_set:
                list_set[i] += 1
            else:
                list_set[i] = 1
        return len(list_set) == len(set(list_set.values()))


def main() -> None:
    arr = [1, 2]
    solution = Solution()
    result = solution.uniqueOccurrences(arr)
    print(result)


if __name__ == "__main__":
    main()
