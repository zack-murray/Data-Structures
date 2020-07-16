from singly_linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class ArrayQueue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    # Check the length of the queue
    def __len__(self):
        return self.size

    # Append value to the end of the queue
    def enqueue(self, value):
        self.storage.append(value)
        self.size += 1

    # Deletes value from front of the queue, returns the value at the front of the queue
    def dequeue(self):
        # If queue is empty, return none
        if self.size == 0:
            return None
        # If queue has values, remove most front value and return new value in front of the queue
        else:
            pop = self.storage.pop(0)
            self.size -= 1 
            return pop

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    # Check the length of the queue
    def __len__(self):
        return self.size

    # Append value to the end of the queue
    def enqueue(self, value):
        # Add input value to end of queue
        self.storage.add_to_tail(value)
        # Increase queue size by 1 for each value added
        self.size += 1

    # Deletes value from front of the queue, returns the value at the front of the queue
    def dequeue(self):
        # If queue is empty, return none
        if self.size == 0:
            return None
            # If queue has values, remove most front value
        else:
            # Decrease queue size by 1 for each value removed
            self.size -= 1
            # Return new value in front of the queue
            return self.storage.remove_head()