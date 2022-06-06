# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
# If the two linked lists have no intersection at all, return null.
# Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Intersected at '2'
# Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
# From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; 
# There are 1 node before the intersected node in B.
  
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setSave = set()
        current = headA # the current interger in list headA   
        while current:
            setSave.add(current)
            current = current.next
        current = headB
        while current:
            if current in setSave:
                return current
            current = current.next
        return None
