# Q 1. In an e-commerce system, customer account IDs are stored in a list, and you are
# tasked with writing a program that implements the following:
# a) Linear Search: Check if a particular customer account ID exists in the list.
# b) Binary Search: Implement Binary search to find if a customer account ID exists,
# a) Improving the search efficiency over the basic linear

cust_id = []

def accept():
    n = int(input("Enter the Number of For how many customer data you want to add :- "))
    for i in range(0, n):
        id = int(input("Enter the Customer ID :- "))
        cust_id.append(id)


def display():
    print(cust_id)


def linear_search():
    if len(cust_id) == 0:
        print("No data to search. Please add customer IDs first.\n")
    else:
        key = int(input("Enter the ID you want to Search :- "))
        for i in range(len(cust_id)):
            if key == cust_id[i]:
                print(f"Customer id {key} found at {i} index")
                print()
                break
        else:
            print(f"Customer id {key} NOT found (linear search).")


def binary_search():
    sorted_data = sorted(cust_id)
    print(f"Performing Binary Search on sorted data: {sorted_data}")
    key = int(input("Enter the ID you want to Search :- "))
    low = 0
    high = len(sorted_data) - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid] == key:
            print(f"The Customer id {key} found at {mid} index")
            found = True
            break
        elif key < sorted_data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if not found:
        print(f"Customer id {key} NOT found (binary search).")


while True:
    print("Menu")
    print("1. Enter the Customer Data ")
    print("2. Display The Customer Data ")
    print("3. Search Through Linear Search")
    print("4. Search Through Binary Search")
    print("5. Exit")
    print()
    choice = int(input("Enter your choice :- "))
    print()

    if choice == 1:
        accept()
    elif choice == 2:
        display()
    elif choice == 3:
        linear_search()
    elif choice == 4:
        binary_search()
    elif choice == 5:
        break