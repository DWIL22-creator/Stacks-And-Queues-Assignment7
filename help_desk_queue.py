# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value): #New nodes are added to the rear of the queue using this method.
        a_node = Node(value)
        if not self.front: #If the queue is empty, the front and rear are set to the node.
            self.front = a_node
            self.rear = a_node
        else: #If the queue is not empty, add the new node to the rear of the queue. The rear becomes the new node.
            self.rear.next = a_node
            self.rear = a_node

    def dequeue(self):
        if not self.front: #If the queue is empty, return None.
            return None
        removed_node = self.front #The removed node is currently the front of the queue.
        self.front = self.front.next #We take the node in the front and move it to the next node.
    
        if not self.front: #If it's not in front, we still return the removed node's value.
            self.front = None

        return removed_node.value #otherwise, we return the value of the removed node.
    
    def peek(self):
        if not self.front:
            return None
        return self.front.value

    def print_queue(self):
        current = self.front
        if not current:
            print("The queue is empty.")
            return
        while current:
            print(f"- {current.value}")
            current = current.next #Updates current to the next node in the queue.


def run_help_desk():
    # Create an instance of the Queue class
    help_desk_queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            help_desk_queue.enqueue(name)
            #help_desk_queue.print_queue()
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            helped_customer = help_desk_queue.dequeue()
            if helped_customer is not None:
                print(f"{helped_customer} was helped.")

        elif choice == "3":
            print(f"Next customer: {help_desk_queue.peek()}")
            #Prints the next customer in the queue by using peek.

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            help_desk_queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
