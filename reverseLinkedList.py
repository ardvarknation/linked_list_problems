# Solution to LeetCode "Reverse Linked List" problem.
# Description:
#   Given the head of a singly-linked list, reverse the list, and return reversed list.

## Solution uses Reverse Linked List algorithm.

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  curr = head
  prev = None

  while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

  return prev
