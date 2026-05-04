class Solution:
    def partition(self, head, x):
        lessDummy = ListNode(0)
        greaterDummy = ListNode(0)

        less = lessDummy
        greater = greaterDummy

        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next

            curr = curr.next

        # Important: end greater list
        greater.next = None

        # Join both lists
        less.next = greaterDummy.next

        return lessDummy.next
