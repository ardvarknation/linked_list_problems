# Solution for LeetCode "Linked List Cycle" problem.
# Description:
#   Given head, the head of a linked list, determine if the linked list has a cycle in it.
#   There is a cycle in a linked list if there is some node in that list that can be reached by
#   continuously following the next pointer. Internally, pos is used to denote the index of 
#   the node that the tail's next pointer is connected to. 
#   Return True if there is a cycle, or False if not.

## Solution uses "Tortoise and hare" algorithm, with two pointers moving at different speeds. 
## This works because, when there is no cycle, the fast pointer will reach the end (null), and
## if there is a cycle, the fast pointer will eventually lap the slow pointer, meaning they
## will meet.

def hasCycle(self, head: Optional[ListNode]) -> bool:
  """
  Returns True if the linked list contains a cycle, or False otherwise.

  @args: head, a node in linked list
  @return: bool 
  """
  slow = head
  fast = head

  while fast is not None and fast.next is not None:
    slow = slow.next         # move by 1
    fast = fast.next.next    # move by 2

    if slow == fast:
      return True            # cycle detected
    return False             # no cycle detected
