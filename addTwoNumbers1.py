# Solution 1 for LeetCode "Add Two Numbers" problem.

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  """
  Function to add two numbers represented by two linked lists.

  @args: l1 and l2, linked lists
  @returns: linked list

  Constraints:
  - The number of nodes in each linked list is in the range [1, 100]
  - 0 <= Node.val <= 9
  - It is guaranteed that the list represents a number that does not have leading zeros

  Complexity:
  - Time: O(max(n, m)) as both linked lists traversed once
  - Space: O(max(n, m)) for new linked list returned as result
  """

  # Create a dummy node pointing at head of list
  dummy = ListNode(0)
  
  # Set pointer (current) to dummy
  current = dummy
  
  # Variable for storing carry from addition
  carry = 0

  # Loop through the lists
  while l1 or l2 or carry:
  
    # Get x and y values for computing sum
    x = l1.val if l1 else 0
    y = l2.val if l2 else 0
    
    # Compute sum
    total = x + y + carry

    # Update carry
    carry = total // 10

    # Create new node and attach to current.next
    current.next = ListNode(total % 10)

    # Move current pointer forward
    current = current.next

    # Move l1 and l2 pointers forward
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None

  # Return the sum
  return dummy.next
  
