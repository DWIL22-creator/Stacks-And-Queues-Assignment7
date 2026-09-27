# Import the Node class you created in node.py
from node import Node

# Implement your Stack class here
class Stack:
    def __init__(self):
        self.top = None #Points to the top of the stack. Currently there is no value that's the top yet.

    def pop(self):
        if len(self.undo_stack) == 0:
            return "No options to undo."
        
        #if not self.top: #Not sure if this is correct...So save this for later..
            #return f""
        
        chosen_node = Node(chosen_node) #A node is created from the node class.
        chosen_node = self.top #The node we want to undo, becomes the top.
        self.top = self.top.next #Moves the top attribute to the next node, since we're getting rid of the current top.
        return chosen_node

    def push(self): #Removes the Node at the top of the stack and returns the value.
        if len(self.redo_stack) == 0:
            return "No options to redo."
        chosen_node = Node(chosen_node) #A node is created from the node class.
        chosen_node.next = self.top #The next node in the stack becomes the top.
        self.top = chosen_node #The top becomes the newly chosen node.
        return chosen_node #Returns the newly chosen node.

    def peek(self): #Returns the value of the node on top without removing it.
        if not self.top:
            return "The stack is empty."

    def print_stack(self): #Prints the current stacks options.
        current = self.top
        if not current:
            print("The stack is empty...")
            return
        while current:
            if input() == 4:
                print(undo_stack)
                current = current.next

            elif input() == 5:
                print(redo_stack)
                current = current.next

def run_undo_redo():
    # Create instances of the Stack class for undo and redo
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
            action.push(undo_stack)
            redo_stack.clear() #Clears the redo stack after performing a new action.
            # Push the action onto the undo stack and clear the redo stack

            print(f"Action performed: {action}")
        elif choice == "2":
            action = undo_stack.pop()
            redo_stack.push(action)
            # Pop an action from the undo stack and push it onto the redo stack
            

        elif choice == "3":
            action = redo_stack.pop()
            undo_stack.push(action)
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

#My stacks undo and redo...
undo_stack = Stack()
redo_stack = Stack()
if __name__ == "__main__":
    run_undo_redo()