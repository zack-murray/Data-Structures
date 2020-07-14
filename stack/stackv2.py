"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    # Initialize class with size of 0 and empty stack/list
    def __init__(self):
        self.size = 0
        self.storage = []
    
    # Check length of self.storage stack/list
    def len(self):
        return len(self.storage)

    # Append value to the end of the stack/list
    def push(self, value):
        self.storage.append(value)

    # Deletes value from end of the stack/list, returns the element at the top of the stack
    def pop(self):
        # For pop and peek methods, check whether stack is empty, to avoid exceptions
        if len(self.storage) > 0:
            return self.storage.pop()
        else:
            return None

# Subclass of LLStack, user will never interface with this class
class Node:
    def __init__(self, value):
        # Where we're storing past data point
        self.value = value
        # Where we're storing pointer to the next node
        self.next = None

class LLStack:
    def __init__(self):
        # Will never contain data(not indexable), placeholder to point to first element in list
        self.head = node()

    # Check length of linked list
    def len(self):
        # Instantiate current variable to point to current node
        current = self.head
        # Instantiate total variable to keep track of total # of nodes
        total = 0
        # Iterate over nodes
        while current.next !=None:
            # Incrementing the total 
            total+=1
            # Traverse to next node until next node = None
            current = current.next
        return total 

    # Create first value of the list/stack, then appends proceeding values to the end
    def push(self, value):
        # Create new node of class node, pass in the value you want to add
        new_node = node(value)
        # Instaniate current variable to point to current node
        current = self.head
        # Iterate over each node(starting with head), when next node = none (last node), 
        # insert new_node as the next node
        while current.next !=None:
            # If not at the end of the list, keep iterating
            current = current.next
        # append new node to the end of the list/stack
        current.next = new_node

    # Deletes last value of the list/stack, returns the element at the top of the stack
    def pop(self):
        # Instaniate current variable to point to current node
        current = self.head
        # Iterate over each node(starting with head), when next node = none (last node), 
        # remove the next node
        while current.next !=None:
            # If not at the end of the list, keep iterating
            current = current.next
        # remove last node at the end of the list/stack
        current.next = 

    
    # Deletes indexed value from linked list
    def pop_index(self, index):
        # Check and make sure index provided is not longer than current len of linked list
        if index >= self.length():
            print(f"ERROR: 'Erase' index out of range!")
            return
        # Instaniate current index variable to point to current index
        current_index = 0
        # Instaniate current variable to point to current node
        current = self.head
        while True:
            # Save current node as last node (when erasing nodes, need to make sure newly adjacent
            # nodes are still connected)
            last_node = current
            # Increment current node by setting it equal to the next node
            current = current.next
            # Check to see if we're at the index that user provided
            if current_index == index:
                # Effectively erases current node
                last_node.next = current.next
                return 
            # If not at current index, increment to reflect the fact current node was incremented
            current_index += 1

    

    
