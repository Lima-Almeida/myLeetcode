class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head) -> bool:
    visited = []
    has_cycle = False
    while head:

        if head in visited:
            has_cycle = True
            break
        else:
            visited.append(head)
            head = head.next

    return has_cycle

root = ListNode(3)
root.next = ListNode(2)
root.next.next = ListNode(0)
root.next.next.next = ListNode(-4)
root.next.next.next.next = root.next

print(hasCycle(root))