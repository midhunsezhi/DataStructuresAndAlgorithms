def RemoveDuplicates(head):
    if head is None:
        return None
    if head.next is None:
    	return head
    
    current = head
    successor = head.next
    while successor is not None:
        if current.data == successor.data:
            successor = successor.next
        else:
	        current.next = successor
	        current = successor
	        successor = successor.next
            
    current.next = successor
            
    return head
  