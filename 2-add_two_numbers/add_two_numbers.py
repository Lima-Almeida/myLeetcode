class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        lista_aux = []
        l1_end = False
        l2_end = False
        carry = False

        while True:
            if l1 == None:
                parcela_l1 = 0
                l1_end = True
            else:
                parcela_l1 = l1.val

            if l2 == None:
                parcela_l2 = 0
                l2_end = True
            else:
                parcela_l2 = l2.val
                
            sum = parcela_l1 + parcela_l2

            if carry:
                sum = sum + 1
                carry = False

            if sum >= 10:
                sum = sum - 10
                carry = True

            if l1_end and l2_end and carry == False and sum != 1:
                break

            lista_aux.append(sum)

            if not l1_end:
                l1 = l1.next

            if not l2_end:
                l2 = l2.next

        print(lista_aux)

        head = ListNode(lista_aux[0])
        current = head
        for k in range(len(lista_aux) - 1):
            current.next = ListNode(lista_aux[k + 1])
            current = current.next

        return head