# Solution for the LeetCode "Intersection of Two Linked Lists" problem.
# Description:
#   Given the heads of two singly-linked lists headA and headB, return the node
#   at which the two lists intersect. If the two linked lists have no intersection
#   at all, return null.
#   The test cases are generated such that there are no cycles anywhere in the
#   entire linked list.
#   The linked lists must retain their original structure after function returns.

# Complexity:
# - Time: O(n + m)
# - Space: O(1)  no extra memory


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#       self.val = x
#       self.next = None
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
  """
  Function returns the intersection of two linked lists, or null if no intersection possible.

  @args: headA, headB - ListNode for head of A and B
  @returns: ListNode containing intersection or null

  Preconditions:
  - The number of nodes of listA is in the m
  - The number of nodes of listB is in the n
  - 1 <= m, n <= 3*10^4
  - 1 <= Node.val <= 10^5
  - 0 <= skipA <= m
  - 0 <= skipB <= n
  - intersectVal is 0 if listA and listB do not intersect
  - intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect
  """

  # If headA or headB is null
  if not headB or not headB:
    return None

  # Initialise two pointers pointer_a and pointer_b to headA and headB
  pointer_a, pointer_b = headA, headB

  # Traverse both lists
  while pointer_a != pointer_b:
    pointer_a = pointer_a.next if pointer_a else headB
    pointer_b = pointer_b.next if pointer_b else headA

  # Return the intersection of two lists
  return pointer_a
