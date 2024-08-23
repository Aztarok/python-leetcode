from typing import List
import heapq

class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "$" + s
        return result
    def decode(self, s: str) -> List[str]:
        result, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result
        
        
def main() -> None:
    strs = ["Hello, World!", "Hello, Coder!", "Hello, Coder, World!"]
    print(strs)
    newStr = Solution().encode(strs)
    print(newStr)
    newStr = Solution().decode(newStr)
    print(newStr)
    
if __name__ == "__main__":
    main()