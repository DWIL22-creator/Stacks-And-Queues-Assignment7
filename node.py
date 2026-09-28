# Implement your Node class here
#Node class implemented.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Design Memo
#1) Why is a stack the right choice for undo/redo?
#A stack is the right choice for my undo/redo system because it allows me to keep track of items in a last-in and first out manner. 
#They're most ideal for this use because we want the most recent action to get handeled first. In this case, it's adding an item to the stack.
#The program primarily back-tracks, pauses, resumes, and rexecutes actions. Which is most ideal in comparison to a queue.

#2) Why is a queue better suited for the help desk?
#A queue is better suited for the help desk because it allows us to manage customers in a first-in and last-out manner.
#The queue moves items along in the order they arrive, ensuring that the first item, is the first to be tackled.
#In this case, we want to ensure that customers are helped in the order they arrive, rather than helping customers at random. 
#Therefore, if we used a queue for the help desk, we would ensure that customers are helped in the order they submitted the tickets, maintaining fairness and priority based on arrival time.

#3)How do your implementations differ from Python’s built-in lists?
#My implementation of stacks and queues differ from Python's built in lists because they're specific to issues that require a particular order of operations, such as undo/redo for stacks and first-in-first-out for queues.
#Built in lists keep track of all elements in a general manner, but they don't enforce the specific order of operations that stacks and queues do.
#