/* Create a Student Record Management System using linked list
• Use a singly/doubly linked list to store student data (Roll No, Name, Marks).
• Perform operations: Add, Delete, Update, Search, and Sort.
• Display records in ascending/descending order based on marks or roll number. */

#include <iostream>
#include <string>
using namespace std;

struct Node
{
    int rollno, marks;
    string name;
    Node *next;
};

Node *head = nullptr;

void addStudent()
{

    Node *newNode = new Node;
    cout << "Enter Roll No. : ";
    cin >> newNode->rollno;
    cout << "Enter Name : ";
    cin.ignore();
    getline(cin, newNode->name);
    cout << "Enter Marks : ";
    cin >> newNode->marks;
    newNode->next = nullptr;

    if (head == nullptr)
    {
        head = newNode;
    }
    else
    {
        Node *temp = head;
        while (temp->next != nullptr)
        {
            temp = temp->next;
        }
        temp->next = newNode;
    }
    cout << "Student added." << endl;
}

void deleteStudent()
{

    if (head == nullptr)
    {
        cout << "List is empty" << endl;
    }

    Node *temp = head;

    int Drollno;
    cout << "Enter Roll No to Delete : ";
    cin >> Drollno;

    if (head->rollno == Drollno)
    {
        head = head->next;
        delete temp;
        cout << "Student Deleted" << endl;
        return;
    }

    Node *prev = head;
    temp = head->next;

    while (temp != nullptr && temp->rollno != Drollno)
    {
        prev = temp;
        temp = temp->next;
    }

    if (temp == nullptr)
    {
        cout << "\nStudent with Roll No " << Drollno << " not found." << endl;
        return;
    }

    prev->next = temp->next;
    delete temp;
    cout << "Student Deleted" << endl;
}

void updateStudent()
{
    if (head == nullptr)
    {
        cout << "List is empty" << endl;
        return;
    }

    Node *temp = head;

    int updatedata;
    cout << "Enter Roll No. : ";
    cin >> updatedata;

    while (temp != nullptr)
    {
        if (temp->rollno == updatedata)
        {
            cout << "Record Found of Roll No. " << temp->rollno << endl;
            cout << "Current Name : " << temp->name << endl;
            cout << "Current Marks : " << temp->marks << endl;

            cout << "Updating...\n Enter New Name : " << endl;
            cin.ignore();
            getline(cin, temp->name);
            cout << "Enter New Marks : " << endl;
            cin >> temp->marks;

            cout << "Student Record Updated" << endl;
            return;
        }
        temp = temp->next;
    }

    cout << "Student with Roll No. " << updatedata << " Not Found" << endl;
}

void searchStudent()
{
    if (head == nullptr)
    {
        cout << "List is empty" << endl;
        return;
    }

    Node *temp = head;

    int search;
    cout << "Enter Roll No. ";
    cin >> search;

    while (temp != nullptr)
    {
        if (temp->rollno == search)
        {
            cout << "Record Found" << endl;
            cout << "Roll No. : " << temp->rollno << endl;
            cout << "Name : " << temp->name << endl;
            cout << "Marks : " << temp->marks << endl;
            return;
        }
        temp = temp->next;
    }

    cout << "Student with Roll No. " << search << " Not Found" << endl;
}
// Use this one - Selection Sort
// It's faster to write in an exam.
void sortList()
{
    if (head == nullptr || head->next == nullptr)
    {
        return;
    }

    // Outer loop 'i' is the "anchor"
    for (Node *i = head; i->next != nullptr; i = i->next)
    {

        // Inner loop 'j' is the "scanner"
        for (Node *j = i->next; j != nullptr; j = j->next)
        {

            // Compare the anchor 'i' to the scanner 'j'
            if (i->rollno > j->rollno)
            {

                // Swap all three data fields
                int tempRoll = i->rollno;
                i->rollno = j->rollno;
                j->rollno = tempRoll;

                string tempName = i->name;
                i->name = j->name;
                j->name = tempName;

                int tempMarks = i->marks;
                i->marks = j->marks;
                j->marks = tempMarks;
            }
        }
    }
}
void display()
{
    if (head == nullptr)
    {
        cout << "List is empty" << endl;
        return;
    }

    Node *temp = head;
    cout << "--------------- All Student Records ---------------" << endl;
    cout << "Roll No. \t\t Name \t\t Marks" << endl;
    cout << "---------------------------------------------" << endl;

    while (temp != nullptr)
    {
        cout << temp->rollno << "\t\t" << temp->name << "\t\t" << temp->marks << endl;
        temp = temp->next;
    }

    cout << "---------------------------------------------" << endl;
}
int main()
{
    int choice;

    do
    {
        cout << "\n\n--- Student Management ---"
             << "\n1. Add"
             << "\n2. Delete"
             << "\n3. Update"
             << "\n4. Search"
             << "\n5. Display All"
             << "\n6. Sort (by Roll No)"
             << "\n0. Exit"
             << "\n--------------------------"
             << "\nEnter choice: ";

        cin >> choice;

        switch (choice)
        {
        case 1:
            addStudent();
            break;
        case 2:
            deleteStudent();
            break;
        case 3:
            updateStudent();
            break;
        case 4:
            searchStudent();
            break;
        case 5:
            display();
            break;
        case 6:
            sortList();
            cout << "\n[Success] List sorted by Roll No." << endl;
            display();
            break;
        case 0:
            cout << "\nExiting. Goodbye!" << endl;
            break;
        default:
            cout << "\n[Error] Invalid choice." << endl;
        }

    } while (choice != 0);

    return 0;
}