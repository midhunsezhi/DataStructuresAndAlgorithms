def has_cycle(head):
    current = head
    jump_2 = head
    while current.next is not None and jump_2 is not None and jump_2.next is not None:
        jump_2 = jump_2.next.next
        if jump_2 == current:
            return 1
        current = current.next
    return 0