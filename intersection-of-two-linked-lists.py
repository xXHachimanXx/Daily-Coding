"""
This problem was asked by Google.

Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the exact same 
node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) 
and constant space.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(headA, headB):
        while headA != None and headB != None:
            if headA is headB:
                return headA.val
            
            headA = headA.next
            headB = headB.next

intersection = ListNode(8)

headA = ListNode(3)
headA.next = ListNode(7)
headA.next.next = intersection
headA.next.next.next = ListNode(10)

headB = ListNode(99)
headB.next = ListNode(1)
headB.next.next = intersection
headB.next.next.next = ListNode(10)

assert Solution.getIntersectionNode(headA, headB) == 8

intersection = ListNode(8)

headA = ListNode(3)
headA.next = ListNode(7)
headA.next.next = ListNode(10)
headA.next.next.next = intersection

headB = ListNode(99)
headB.next = ListNode(1)
headB.next.next = intersection
headB.next.next.next = intersection

assert Solution.getIntersectionNode(headA, headB) == 8

intersection = ListNode(8)

headA = ListNode(3)
headA.next = ListNode(7)
headA.next.next = ListNode(10)
headA.next.next.next = intersection

headB = ListNode(99)
headB.next = ListNode(1)
headB.next.next = intersection
headB.next.next.next = ListNode(3)

assert Solution.getIntersectionNode(headA, headB) == None