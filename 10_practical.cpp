// A list stores city names and their populations. Use a Binary Search Tree for implementation.
// Provide a facility for adding new cities, deleting a city, and updating population values.
// Provide a facility to display all the city names in ascending/descending order.
// Also, find how many maximum comparisons are required to search for a particular city.

#include <iostream>
#include <string>
using namespace std;

// ------------------ Node Structure ------------------
struct Node
{
    string city;
    int population;
    Node *left;
    Node *right;
};

// ------------------ Create a New Node ------------------
Node *createNode(string cityname, int populations)
{
    Node *newNode = new Node();
    newNode->city = cityname;
    newNode->population = populations;
    newNode->left = nullptr;
    newNode->right = nullptr;
    return newNode;
}

// ------------------ Insert Node ------------------
Node *insertCity(Node *root, string cityName, int populations)
{
    if (root == nullptr)
    {
        return createNode(cityName, populations);
    }

    if (cityName < root->city)
    {
        root->left = insertCity(root->left, cityName, populations);
    }
    else if (cityName > root->city)
    {
        root->right = insertCity(root->right, cityName, populations);
    }
    else
    {
        cout << "City " << cityName << " already exists! Use update to change population.\n";
    }

    return root;
}

// ------------------ Search Node ------------------
Node *searchCity(Node *root, string cityName)
{
    if (root == nullptr || root->city == cityName)
    {
        return root;
    }

    if (cityName < root->city)
    {
        return searchCity(root->left, cityName);
    }
    else
    {
        return searchCity(root->right, cityName);
    }
}

// ------------------ Update Population ------------------
void updatePopulations(Node *root, string cityName, int newPop)
{
    Node *target = searchCity(root, cityName);

    if (target != nullptr)
    {
        target->population = newPop;
        cout << "Population of " << cityName << " updated to " << newPop << ".\n";
    }
    else
    {
        cout << "City " << cityName << " not found. Cannot update population.\n";
    }
}

// ------------------ Find Inorder Successor  ------------------
Node *getInorderSuccessor(Node *root)
{
    Node *current = root;
    while (current && current->left != nullptr)
        current = current->left;
    return current;
}

// ------------------ Delete City ------------------
Node *deleteCity(Node *root, string cityName)
{
    if (root == nullptr)
    {
        return nullptr;
    }

    if (cityName < root->city)
    {
        root->left = deleteCity(root->left, cityName);
    }
    else if (cityName > root->city)
    {
        root->right = deleteCity(root->right, cityName);
    }
    else
    {
        // Case 1 & 2: One child or no child
        if (root->left == nullptr)
        {
            Node *temp = root->right;
            delete root;
            return temp;
        }
        else if (root->right == nullptr)
        {
            Node *temp = root->left;
            delete root;
            return temp;
        }
        // Case 3: Two children
        else
        {
            Node *IS = getInorderSuccessor(root->right);

            // Copy successor's data to this node
            root->city = IS->city;
            root->population = IS->population;

            // Delete the successor from the right subtree
            root->right = deleteCity(root->right, IS->city);
        }
    }
    return root;
}

// ------------------ Display in Ascending Order (Inorder) ------------------
void displayAscending(Node *root)
{
    if (root != nullptr)
    {
        displayAscending(root->left);                             // Left
        cout << root->city << " (" << root->population << ") | "; // Root
        displayAscending(root->right);                            // Right
    }
}

// ------------------ Display in Descending Order (Reverse Inorder) ------------------
void displayDescending(Node *root)
{
    if (root != nullptr)
    {
        displayDescending(root->right);                           // Right
        cout << root->city << " (" << root->population << ") | "; // Root
        displayDescending(root->left);                            // Left
    }
}

// ------------------ Max Comparisons (Height) ------------------
int maxComparisons(Node *root)
{
    if (root == nullptr)
        return 0;

    int leftHeight = maxComparisons(root->left);
    int rightHeight = maxComparisons(root->right);

    // Height = 1 + max(leftHeight, rightHeight)
    return 1 + (leftHeight > rightHeight ? leftHeight : rightHeight);
}

// ------------------ MAIN PROGRAM (Driver Code) ------------------
int main()
{
    Node *root = nullptr;
    int choice, population;
    string cityname;

    // Initial data insertion (Example data)
    root = insertCity(root, "Delhi", 19000000);
    root = insertCity(root, "Mumbai", 20000000);
    root = insertCity(root, "Bangalore", 13000000);
    root = insertCity(root, "Kolkata", 15000000);
    root = insertCity(root, "Chennai", 10000000);

    while (true)
    {
        cout << "\n\nBST City Database Menu \n";
        cout << "1. Add New City\n";
        cout << "2. Delete City\n";
        cout << "3. Update Population\n";
        cout << "4. Display Cities (Ascending Order)\n";
        cout << "5. Display Cities (Descending Order)\n";
        cout << "6. Find Max Comparisons for Search\n";
        cout << "7. Exit\n";
        cout << "Enter your choice: ";

        // Simplified input handling
        cin >> choice;

        switch (choice)
        {
        case 1:
            cout << "Enter City Name: ";
            cin >> cityname;
            cout << "Enter Population: ";
            cin >> population;
            root = insertCity(root, cityname, population);
            break;

        case 2:
            cout << "Enter City Name to Delete: ";
            cin >> cityname;
            root = deleteCity(root, cityname);
            cout << "Deletion attempt finished for " << cityname << ".\n";
            break;

        case 3:
            cout << "Enter City Name to Update: ";
            cin >> cityname;
            cout << "Enter New Population: ";
            cin >> population;
            updatePopulations(root, cityname, population);
            break;

        case 4:
            cout << "\n--- Cities in ASCENDING Order (by Name) ---\n";
            if (root == nullptr)
            {
                cout << "Database is empty.";
            }
            else
            {
                displayAscending(root);
            }
            cout << endl;
            break;

        case 5:
            cout << "\n--- Cities in DESCENDING Order (by Name) ---\n";
            if (root == nullptr)
            {
                cout << "Database is empty.";
            }
            else
            {
                displayDescending(root);
            }
            cout << endl;
            break;

        case 6:
            cout << "\nMaximum comparisons required for search (Worst Case): "
                 << maxComparisons(root) << endl;
            break;

        case 7:
            cout << "Exiting program...\n";
            return 0;

        default:
            cout << "Invalid choice!\n";
        }
    }
}