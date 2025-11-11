# Design and implement a hash table of fixed size.
# Use the division method for the hash function and resolve collisions using linear probing.
# Allow the user to perform the following operations:
# • Insert a key
# • Search for a key
# • Delete a key
# • Display the table

class hashtable:

    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None and self.table[index] != "DELETED":
            if self.table[index] == key:
                print(f"Key {key} already exists.")
                return

            index = (index + 1) % self.size
            if index == start:
                print("Hash Table is Full")
                return

        self.table[index] = key
        print("Key inserted successfully")
        self.display()

    def search(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                print(f"Key {key} found at index {index}")
                return

            index = (index + 1) % self.size

            if start == index:
                break

        print("Key not found")

    def delete(self, key):
        index = self.hash_function(key)
        start = index

        while self.table[index] is not None:
            if self.table[index] == key:
                self.table[index] = "DELETED"
                print("key deleted successfully")
                self.display()
                return

            index = (index + 1) % self.size

            if index == start:
                break

        print("key not found")

    def display(self):
        print("\nhash table:")
        for i in range(self.size):
            print(f"{i} : {self.table[i]}")
        print("_" * 30)


hash_table = hashtable()

while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert key")
    print("2. Search key")
    print("3. Delete key")
    print("4. Display hash table")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        key = int(input("Enter key (integer): "))
        hash_table.insert(key)

    elif choice == "2":
        key = int(input("Enter key to search: "))
        hash_table.search(key)

    elif choice == "3":
        key = int(input("Enter key to delete: "))
        hash_table.delete(key)

    elif choice == "4":
        hash_table.display()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
