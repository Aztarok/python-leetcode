from typing import List

# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         numbers: dict = {}
#         for i, num in enumerate(nums1):
#             if num not in numbers:
#                 numbers[num] = 1
#             else:
#                 numbers[num] += 1
#         for i, num in enumerate(nums2):
#             if num not in numbers:
#                 numbers[num] = 1
#             else:
#                 numbers[num] -= 1
#         result = [[], []]
#         for key in numbers:
#             if numbers[key] > 0:
#                 if key in nums1:
#                     result[0].append(key)
#                 else:
#                     result[1].append(key)
#         return result


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        in_nums1 = set(nums1)
        in_nums2 = set(nums2)
        result = [
            list(set(in_nums1) - set(in_nums2)),
            list(set(in_nums2) - set(in_nums1)),
        ]
        return result


def main() -> None:
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    solution = Solution()
    result = solution.findDifference(nums1, nums2)
    print(result)


if __name__ == "__main__":
    main()
