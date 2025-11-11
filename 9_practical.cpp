// Implement various operations on a Binary Search Tree, such as insertion, deletion, display, and search.

#include <iostream>
using namespace std;

// ------------------ Node Structure ------------------
struct Node
{
    int data;
    Node *left;
    Node *right;
};

// ------------------ Create a New Node ------------------
Node *createNode(int value)
{
    Node *newNode = new Node();
    newNode->data = value;
    newNode->left = nullptr;
    newNode->right = nullptr;
    return newNode;
}

// ------------------ Insert Node ------------------
Node *insert(Node *root, int value)
{
    if (root == nullptr)
    {
        return createNode(value);
    }

    if (value < root->data)
    {
        root->left = insert(root->left, value);
    }
    else if (value > root->data)
    {
        root->right = insert(root->right, value);
    }

    return root;
}

// ------------------ Inorder Display ------------------
void inorder(Node *root)
{
    if (root == nullptr)
    {
        return;
    }

    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

// ------------------ Search Node ------------------
bool search(Node *root, int key)
{
    if (root == nullptr)
    {
        return false;
    }

    if (root->data == key)
    {
        return true;
    }

    if (key < root->data)
    {
        return search(root->left, key);
    }
    else
    {
        return search(root->right, key);
    }
}

// ------------------ Find Inorder Successor ------------------
Node *getInorderSuccessor(Node *root)
{
    // The inorder successor is the leftmost node in the right subtree
    while (root != nullptr && root->left != nullptr)
    {
        root = root->left;
    }
    return root;
}

// ------------------ Delete Node ------------------
Node *deleteNode(Node *root, int key)
{
    if (root == nullptr)
    {
        return nullptr;
    }

    // 1. Traverse to find the node
    if (key < root->data)
    {
        root->left = deleteNode(root->left, key);
    }
    else if (key > root->data)
    {
        root->right = deleteNode(root->right, key);
    }
    else
    {
        // 2. Node found! Handle the three cases:

        // Case 1: Node with only right child or no child
        if (root->left == nullptr)
        {
            Node *temp = root->right;
            delete root; // Deallocate memory
            return temp;
        }
        // Case 2: Node with only left child
        else if (root->right == nullptr)
        {
            Node *temp = root->left;
            delete root; // Deallocate memory
            return temp;
        }
        // Case 3: Node with two children
        else
        {
            // Find the inorder successor (smallest node in the right subtree)
            Node *IS = getInorderSuccessor(root->right);

            // Copy the inorder successor's content to this node
            root->data = IS->data;

            // Delete the inorder successor from the right subtree
            root->right = deleteNode(root->right, IS->data);
        }
    }
    return root;
}

// ------------------ MAIN PROGRAM (Driver Code) ------------------
int main()
{
    Node *root = nullptr;
    int choice, value;

    while (true)
    {
        cout << "\nBinary Search Tree Menu\n";
        cout << "1. Insert Node\n";
        cout << "2. Delete Node\n";
        cout << "3. Search Node\n";
        cout << "4. Display (Inorder)\n";
        cout << "5. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "Enter value to insert: ";
            cin >> value;
            root = insert(root, value);
            cout << "Value " << value << " inserted.\n";
            break;
        case 2:
            cout << "Enter value to delete: ";
            cin >> value;
            root = deleteNode(root, value);
            cout << "Attempted to delete " << value << ".\n";
            break;
        case 3:
            cout << "Enter value to search: ";
            cin >> value;
            if (search(root, value))
                cout << "Value " << value << " found!\n";
            else
                cout << "Value " << value << " not found!\n";
            break;
        case 4:
            cout << "BST Inorder Traversal (Sorted): ";
            if (root == nullptr)
            {
                cout << "Tree is empty.\n";
            }
            else
            {
                inorder(root);
                cout << endl;
            }
            break;
        case 5:
            cout << "Exiting program...\n";
            return 0;
        default:
            cout << "Invalid choice!\n";
        }
    }
}