from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index, read_index, length = 0, 0, len(chars)
        while read_index < length:
            current = chars[read_index]
            count = 0
            while read_index < length and chars[read_index] == current:
                read_index += 1
                count += 1
            chars[write_index] = current
            write_index += 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        return write_index


def main() -> None:
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    solution = Solution()
    result = solution.compress(chars)
    print(result)


if __name__ == "__main__":
    main()
