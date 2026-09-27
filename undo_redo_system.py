# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None #Points to the top of the stack. Currently there is no value that's the top yet.

    def pop(self):
        if self.top is None:
            return "No options to undo."
        chosen_node = self.top.chosen_node #A node is chosen and stored in the variable chosen_node.
        self.top = self.top.next #It takes the top node, and movies it to the next node.
        return chosen_node #It then choses the node that was originally at the top of the stack.
        
        

    def push(self): #Removes the Node at the top of the stack and returns the value.
        #if len(self.redo_stack) == 0:
            #return "No options to redo."
        a_node = Node(a_node) #A node is created from the node class.
        a_node.next = self.top #The next node in the stack becomes the top.
        self.top = a_node #The top becomes the newly chosen node.
        #return a_node #Returns the newly chosen node.

    def peek(self): #Returns the value of the node on top without removing it.
        if not self.top is None:
            return "The stack is empty."
        return self.top.chosen_node  #Returns the node at the top.

    def print_stack(self): #Prints the current stacks options.
        current = self.top
        if current is None:
            print("The stack is empty.")
            return
        while current: #Not sure if this is correct...
            print(current.chosen_node)
            current = current.next

            #if input() == 4:
                #print(current.undo_stack) #I don't know if this is correct... *FIX LATER*

            #elif input() == 5:
                #print(current.redo_stack) #I don't know if this is correct... *FIX LATER*
                #current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
    undo_stack = Stack()
    redo_stack = Stack()
    #Do I put undo_stack = Stack() and redo_stack = Stack() here?
    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")
            undo_stack.push(action)
            redo_stack.Stack() #Clears the redo stack after performing a new action.
            # Push the action onto the undo stack and clear the redo stack

            print(f"Action performed: {action}")
        elif choice == "2":
            undo_stack.pop()
            undo_stack.push(redo_stack)
            # Pop an action from the undo stack and push it onto the redo stack
            

        elif choice == "3":
            action =redo_stack.pop()
            if action != "The stack is empty.":
                redo_stack.push(undo_stack)
            # Pop an action from the redo stack and push it onto the undo stack


        elif choice == "4":
            # Print the undo stack
            print("\nUndo Stack:")
            undo_stack.print_stack()


        elif choice == "5":
            # Print the redo stack
            print("\nRedo Stack:")
            redo_stack.print_stack()
            
    
        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_undo_redo()