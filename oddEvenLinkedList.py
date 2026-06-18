# Solution for LeetCode "Odd Even Linked List" problem.
# Description:
#   Given the head of a singly-linked list, group all the nodes with odd indices together followed by the nodes 
#   with even indices, and return the reordered list.
#   The first node is considered odd (not its value), and second is even, and so on.
#   The relative order of both the even and odd groups should remain as it was in the input.
#   You must solve the problem in O(1) extra space and O(n) time complexity.
# Complexity:
# - Time: O(n)  traverses list once
# - Space: O(1)  in-place rearrangement

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, val=0, next=None):
#      self.val = val
#      self.next = next
def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  """
  Function groups all the nodes of linked list with odd indices together followed by
  nodes with even indices, and returns the reordered list.

  @args: head, Node of singly linked list
  @returns: ListNode of reordered list

  Preconditions:
  - The number of nodes in the linked list is in the range [0, 10^4]
  - -10^6 <= Node.val <= 10^6
  """
  
  # Check for edge cases where list is empty or only a single node
  if head == None:
    return None

  # Initialise two pointers - odd and even
  odd = head
  even = head.next

  # Store start of even list for attaching later
  evenHead = even

  # Iterate through the list
  while even and even.next:
    # Link odd nodes
    odd.next = even.next
    odd = odd.next

    # Link even nodes
    even.next = odd.next
    even = even.next

  # Update odd.next with evenHead
  odd.next = evenHead

  # Return the head of the list
  return head
