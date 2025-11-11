# Implement a real-time event processing system using a Queue data structure.
# The system should support the following features:
# • Add an Event: When a new event occurs, it should be added to the event queue.
# • Process the Next Event: The system should process and remove the event that has been in the queue the longest.
# • Display Pending Events: Show all the events currently waiting to be processed.
# • Cancel an Event: An event can be canceled if it has not been processed.


class Event:

    def __init__(self):
        self.queue = []

    def add_event(self, event):

        self.queue.append(event)
        print(f"Event {event} added")
        print()

    def process_event(self):
        if not self.queue:
            print("No events to process")
            return
        processed_event = self.queue.pop(0)
        print(f"Processing Event : {processed_event}")

    def display(self):
        if not self.queue:
            print("Nothing to Display Event")
            return
        else:
            n = 1
            print("Pending Events :- ")
            for i in self.queue:
                print(f"{n}. {i}")
                n += 1

    def cancel_event(self, cname):
        if cname in self.queue:
            self.queue.remove(cname)
            print(f"Event '{cname}' canceled successfully.")
        else:
            print(f"Event {cname} not found in Queue")


a = Event()

while True:

    print()
    print("Real Time Event Processing System")
    print("1. Add an Event")
    print("2. Process the Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")
    print()

    ch = int(input("Enter the choice : "))
    if ch == 1:
        event = input("Enter the Event Name: ")
        a.add_event(event)
    elif ch == 2:
        a.process_event()
    elif ch == 3:
        a.display()
    elif ch == 4:
        cname = input("Enter the Event Name to Cancel: ")
        a.cancel_event(cname)
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice. Please enter between 1-5.\n")
