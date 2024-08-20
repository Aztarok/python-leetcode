from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        while len(result) < k:
            result.append(heapq.heappop(heap)[1])
        return result
        
def main() -> None:
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums, k))

if __name__ == "__main__":
    main()