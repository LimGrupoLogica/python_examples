from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def mergeTwoLists( list1: Optional[ListNode], list2: Optional[ListNode]):
        lista1 = []
        lista2 = []
        current1 = list1
        current2 = list2
        while current1 is not None:
            lista1.append(current1.val)
            current1 = current1.next
        while current2 is not None:
            lista2.append(current2.val)
            current2 = current2.next

        lista1.sort()
        lista2.sort()
        lista1.extend(lista2)
        lista1.sort()
        print(lista1)
        resultado = ListNode()
        current = resultado
        for value in lista1:
            print(value)
            resultado.next = ListNode(value)
            current = resultado.next

        return resultado
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next = ListNode(4)
head2 = ListNode(2)
print(Solution.mergeTwoLists(head1,head2))

    