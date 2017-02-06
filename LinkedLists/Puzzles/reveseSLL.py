
def Reverse(head):
    if head == None:
        return head
 
    prev = None
    current = head
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
        
    head = prev
    return head