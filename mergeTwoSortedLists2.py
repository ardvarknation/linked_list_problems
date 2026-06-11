# Solution 2 for LeetCode "Merge Two Sorted Lists" problem.
# Description:
#  You are given the head's of two linked lists, list1 and list2.
#  Merge the two lists into one sorted list. This list should be made
#  by splicing together the nodes of the first two lists.
#  Return the head of the merged linked list.

## Solution uses recursion calls.

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  """
  Return linked list produced from merging list1 and list2 and sorting.

  @args: list1 and list2, linked list nodes
  @returns: linked list
  """
  # Check base case
  if not list1:
    return list2
  if not list2:
    return list1

  # Recursively call mergeTwoLists() function to merge lists
  if list1.val <= list2.val:
    list1.next = mergeTwoLists(list1.next, list2)  # recursive call
    return list1
  else:
    list2.next = mergeTwoLists(list1, list2.next)  # recursive call
    return list2

