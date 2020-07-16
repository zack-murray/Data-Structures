"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        elif self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # Create new node with specified value 
        new_node = ListNode(value=value)
        # Increase list size by 1 for each node added
        self.length += 1
        # Checking for empty linked list, setting head and tail to new node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        # Assuming the head is already referring to a node
        else:
            # Set the old head's next to refer to the new node
            new_node.next = self.head
            # Reassign old head to previous node  
            self.head.prev = new_node
            # Reassign self.head to refer to the new node 
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # Instantiate the head value
        value = self.head.value
        # Delete that head node from the list
        self.delete(self.head)
        # Return the value of the removed node
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # Create new node with specified value 
        new_node = ListNode(value=value)
        # Increase list size by 1 for each node added
        self.length += 1
        # Checking for empty linked list, setting head and tail to new node
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        # Assuming the tail is already referring to a node
        else:
            # Set the old tail's next to refer to the new node
            new_node.prev = self.tail
            # Reassign old tail to the next node
            self.tail.next = new_node
            # Reassign self.tail to refer to the new node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # Instantiate the tail value
        value = self.tail.value
        # Delete that tail node from the list
        self.delete(self.tail)
        # Return the value of the removed node
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # Checking to see if input node is already the head node
        if node is self.head:
            return
        # Instantiate node value to be moved 
        value = node.value
        # Checking to see if input node is the tail 
        if node is self.tail:
            # If it is, remove it from the tail 
            self.remove_from_tail()
        else:
            # If it's neither head or tail, but still a node in the list, delete
            node.delete()
            # Decrease list size by 1 for the removed node
            self.length -= 1
        # Insert removed node as the new head node of the list
        self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # Checking to see if input node is already the tail node
        if node is self.tail:
            return
        # Instantiate node value to be moved
        value = node.value
        # Checking to see if input node is the head
        if node is self.head:
            # If it is, remove it from the head
            self.remove_from_head()
            # Then insert it to the tail 
            self.add_to_tail(value)
        else:
            # If it's neither head or tail, but still a node in the list, delete
            node.delete()
            # Decrease list size by 1 for the removed node
            self.length -= 1
            # Insert removed node as the new head node of the list
            self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # Decrease list size by 1 for the removed node
        self.length -= 1
        # Checking for empty linked list 
        if not self.head and not self.tail:
            return
        # Checking for one node, if so set both head and tail to none
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Checking to see if node to be deleted is the head
        elif self.head == node:
            # Assigning node next to it to be the new head
            self.head = node.next
            # Remove the original head node
            node.delete()
        # Checking to see if node to be deleted is the tail 
        elif self.tail == node:
            # Assign previous node as the new tail
            self.tail = node.prev
            # Remove the original tail node
            node.delete()
        else:
            node.delete()

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # Checking to make sure you're indexed at the head
        if not self.head:
            return None
        # Instantiate max value as the head value
        max_val = self.head.value
        # Set current value to the head value
        current = self.head
        while current:
            # If the current value is greater than the max value
            if current.value > max_val:
                # Make it so the max value is the new head value
                max_val = current.value
            current = current.next
        # Return the maximum value in the list
        return max_val