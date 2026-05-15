import heapq

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Step 1: put first node of every list in heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        # Step 2: always take smallest node
        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            # Step 3: push next node of same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
