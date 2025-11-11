# Implementing a real-time undo/redo system for a text editing application using a Stack data
# structure. The system should support the following operations:
# • Make a Change: A new change to the document is made.
# • Undo Action: Revert the most recent change and store it for potential redo.
# • Redo Action: Reapply the most recently undone action.
# • Display Document State: Show the current state of the document after undoing or redoing an action


class texteditor:

    def __init__(self):
        self.docs = ""
        self.undo = []
        self.redo = []

    def make_change(self, change):
        self.undo.append(self.docs)
        self.docs += change
        self.redo.clear()
        print("Change made")

        self.display()

    def undo_action(self):
        if not self.docs:
            print("Nothing to undo")
            return

        self.redo.append(self.docs)
        self.docs = self.undo.pop()
        print("Undo Performed")
        self.display()

    def redo_action(self):
        if not self.redo:
            print("Nothing to redo")
            return

        self.undo.append(self.docs)
        self.docs = self.redo.pop()
        print("Redo Performed")
        self.display()

    def display(self):
        print(f"\nThe Current State of Document : {self.docs}")


editor = texteditor()

while True:
    print()
    print("Menu")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")
    print()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        text = input("Enter text to add: ")
        editor.make_change(text)
    elif choice == 2:
        editor.undo_action()
    elif choice == 3:
        editor.redo_action()
    elif choice == 4:
        editor.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
        print()
