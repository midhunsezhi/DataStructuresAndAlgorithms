def GetNode(head, position):
    current, node = head, head
    for _ in range(position):
        current = current.next


    while current.next is not None:
        current = current.next
        node = node.next


    return node