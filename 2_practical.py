# In a company, employee salaries are stored in a list as floating-point numbers. Write a Python
# program that sorts the employee salaries in ascending order using the following two algorithms:
# a) Selection Sort: Sort the salaries using the selection sort algorithm.
# b) Bubble Sort: Sort the salaries using the bubble sort algorithm.
# After sorting the salaries, the program should display top five highest salaries in the company

emp = []

def add_details():
    n = int(input("Enter the No. of Employee you want to add data : "))
    for i in range(0, n):
        m = float(input(f"Enter the Salary of Employee ID {i + 1}: "))
        emp.append(m)

def display_details():
    print("\nEmployee Salaries:")
    for i, salary in enumerate(emp, start=1):
        print(f"ID {i} Salary: {salary}")
    print()

# -------------------- Bubble Sort --------------------
def bubble_sort():
    print("\nSorting using Bubble Sort...")
    n = len(emp)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if emp[j] > emp[j + 1]:
                emp[j], emp[j + 1] = emp[j + 1], emp[j]   # swap

    print("Salaries sorted in ascending order:", emp)
    print("\nTop 5 highest salaries:")
    # reverse the sorted list to get top 5
    top_five = sorted(emp, reverse=True)[:5]
    print(top_five)
    print()

# -------------------- Selection Sort --------------------
def selection_sort():
    print("\nSorting using Selection Sort...")
    n = len(emp)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if emp[j] < emp[min_index]:
                min_index = j
        emp[i], emp[min_index] = emp[min_index], emp[i]  # swap

    print("Salaries sorted in ascending order:", emp)
    print("\nTop 5 highest salaries:")
    top_five = sorted(emp, reverse=True)[:5]
    print(top_five)
    print()

# -------------------- Menu --------------------
while True:
    print("Menu")
    print("1. Enter the Employee Details")
    print("2. Display the Employee Details")
    print("3. Sort Using Bubble Sort")
    print("4. Sort Using Selection Sort")
    print("5. Exit\n")

    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        add_details()
    elif ch == 2:
        display_details()
    elif ch == 3:
        bubble_sort()
    elif ch == 4:
        selection_sort()
    elif ch == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid Choice\n")