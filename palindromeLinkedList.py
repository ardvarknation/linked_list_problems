# Solution to the LeetCode "Palindrome Linked List" problem.
# Description:
#    Given the head of a singly-linked list, return true if it is a palindrome, and false otherwise.

def isPalindrome(self, head: Optional[ListNode]) -> bool:
  """
  Return True if list is a palindrome, False otherwise.

  @args: head, linked list node
  @returns: bool
  """
  if not head or not head.next:
    return True

  # Step 1: Find the middle of the list
  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  # Step 2: Reverse second half
  prev = None
  while slow:
    next_node = slow.next
    slow.next = prev
    prev = slow
    slow = next_node

  # Step 3: Compare the halves
  left = head
  right = prev

  while right:
    if left.val != right.val:
      return False
    left = left.next
    right = right.next

  return True
  
