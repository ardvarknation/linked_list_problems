# Solution 2 for LeetCode "Add Two Numbers" problem.
# Uses in-place approach, instead of creating new list, reuses one of existing lists.
# NOTE: Not always permitted or recommended, but demonstrates knowledge of saving space complexity.

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  """
  Solution #2 for LeetCode "Add Two Numbers" problem.
  Uses in-place modification to save memory.

  @args: l1 and l2, linked lists
  @returns: l1 modified in-place

  Constraints: 
  - The number of nodes in each linked list is in the range [1, 100]
  - 0 <= Node.val <= 9
  - It is guaranteed that the list represents a number that does not have leading zeros

  Complexity:
  - Time: O(max(m, n))
  - Space: O(m)
  """
  # Initialise head pointing to l1
  head = l1

  # Variable to store carry from addition
  carry = 0

  # Previous pointer
  prev = None

  # Loop through both lists
  while l1 or l2:

    # Get x and y values for computing sum
    if l1:
      x = l1.val
    else:
      x = 0
      l1 = ListNode(0)
      prev.next = l1

    y = l2.val if l2 else 0

    # Compute sum
    total = x + y + carry

    # Update carry 
    carry = total // 10

    # Modify l1.val directly with new value
    l1.val = total % 10

    # Move pointers forward
    prev = l1
    l1 = l1.next
    l2 = l2.next if l2 else None

  # Add carry if present
  if carry:
    prev.next = ListNode(carry)

  # Return head of output list containing sum
  return head
  
