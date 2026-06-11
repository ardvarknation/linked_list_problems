# Solution 1 for LeetCode "Merge Two Sorted Lists" problem.
# Description:
#  You are given the head's of two linked lists, list1 and list2.
#  Merge the two lists into one sorted list. This list should be made
#  by splicing together the nodes of the first two lists.
#  Return the head of the merged linked list.

## Solution uses Two-Pointer technique.

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  """
  Return linked list produced from merging list1 and list2 and sorting.

  @args: list1 and list2, linked list nodes
  @returns: linked list

  Complexity:
  - Space and time: O(n + m)
  """
  dummy = ListNode(0)
  current = dummy

  # While nodes remain in lists
  while list1 and list2:
    # Compare the head of both lists
    if list1.val <= list2.val:
      current.next = list1            # attach smaller node to current.next
      list1 = list1.next              # move pointer forward
    else:
      current.next = list2            # attach smaller node
      list2 = list2.next              # move pointer forward

    current = current.next            # move current forward

  # Attach remaining part of other list
  if list1:
    current.next = list1
  else:
    current.next = list2

  return dummy.next
