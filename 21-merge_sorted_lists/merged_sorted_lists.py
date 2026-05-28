class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    aux = ListNode()
    current = aux
    while True:
        if not list1 or not list2:
            break
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next
    
    if list1:
        current.next = list1
    if list2:
        current.next = list2
            
    return aux.next


# Lista 1: [1, 2, 4]
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Lista 2: [1, 3, 4]
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


# Chamada da função
merged = mergeTwoLists(list1, list2)
