def ReversePrint(head):
    if head is not None:
        ReversePrint(head.next)
        print(head.data)
