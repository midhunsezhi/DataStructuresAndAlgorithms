def Reverse(head):
    q = p = head
    while p != None:
        q = p
        p = p.next
        q.next = q.prev
        q.prev = p
    return q