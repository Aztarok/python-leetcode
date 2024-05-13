from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first = head
        second = head.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        head.next = None
        return first


def listToListNode(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def listNodeToList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def main():
    head = listToListNode([1, 2, 3, 4, 5])
    solution = Solution()
    result = solution.reverseList(head)
    print(listNodeToList(result))


if __name__ == "__main__":
    main()
