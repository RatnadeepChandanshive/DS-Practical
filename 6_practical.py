# Implement a hash table of size 10 and use the division method as a hash function.
# In case of a collision, use chaining. Implement the following operations:
# • Insert(key): Insert key-value pairs into the hash table.
# • Search(key): Search for the value associated with a given key.
# • Delete(key): Delete a key-value pair from the hash table.


class HashTable:

    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print("Key updated successfully")
                return

        self.table[index].append([key, value])
        print("Key-value pair inserted successfully")
        self.display()

    def search(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                print(f"{key} : {pair[1]}")
                return

        print(f"Key {key} not found in hash table")

    def delete(self, key):
        index = self.hash_function(key)

        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f"key {key} deleted successfully")
                self.display()
                return

        print(f"Key {key} not found in hash table")

    def display(self):
        print("\n--- Current Hash Table State ---")
        for i in range(self.size):
            print(f"Index {i}: {self.table[i]}")

        print("_" * 30)


hash_table = HashTable()

while True:

    print("\n--- Hash Table Menu ---")
    print("1. Insert key-value pair")
    print("2. Search key")
    print("3. Delete key")
    print("4. Display hash table")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        try:
            key = int(input("Enter key (must be an integer): "))
            value = input("Enter value: ")
            hash_table.insert(key, value)
        except ValueError:
            print("Invalid key. Key must be an integer.")

    elif choice == 2:
        try:
            key = int(input("Enter key to search: "))
            hash_table.search(key)
        except ValueError:
            print("Invalid key. Key must be an integer.")

    elif choice == 3:
        try:
            key = int(input("Enter key to delete: "))
            hash_table.delete(key)
        except ValueError:
            print("Invalid key. Key must be an integer.")

    elif choice == 4:
        hash_table.display()

    elif choice == 5:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")