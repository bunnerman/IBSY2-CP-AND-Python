#include <iostream>
using namespace std;

#define MAX 100 // Maximum size of the stack

class ArrayStack {
private:
    int top;
    int arr[MAX];

public:
    ArrayStack() { 
        top = -1; // Initialize stack as empty
    }

    // Push operation: Add an element to the top
    bool push(int x) {
        if (top >= (MAX - 1)) {
            cout << "Stack Overflow" << endl;
            return false;
        } else {
            arr[++top] = x;
            cout << x << " pushed into stack" << endl;
            return true;
        }
    }

    // Pop operation: Remove the top element
    int pop() {
        if (top < 0) {
            cout << "Stack Underflow" << endl;
            return 0;
        } else {
            int x = arr[top--];
            return x;
        }
    }
};

int main() {
    ArrayStack s;
    s.push(10);
    s.push(20);
    cout << s.pop() << " popped from stack" << endl;
    return 0;
}





#include <iostream>
using namespace std;

// Node structure for the Linked List
struct Node {
    int data;
    Node* next;
};

class LinkedListStack {
private:
    Node* top;

public:
    LinkedListStack() { 
        top = nullptr; 
    }

    // Push operation: Insert at the beginning (head)
    void push(int data) {
        Node* newNode = new Node();
        newNode->data = data;
        newNode->next = top; // New node points to the current top
        top = newNode;       // New node becomes the new top
        cout << data << " pushed to stack" << endl;
    }

    // Pop operation: Remove from the beginning (head)
    int pop() {
        if (top == nullptr) {
            cout << "Stack Underflow" << endl;
            return -1;
        }
        Node* temp = top;
        int poppedData = temp->data;
        top = top->next;     // Move top to the next node
        delete temp;         // Free memory
        return poppedData;
    }

    // Destructor to clean up memory
    ~LinkedListStack() {
        while (top != nullptr) {
            pop();
        }
    }
};

int main() {
    LinkedListStack s;
    s.push(100);
    s.push(200);
    s.push(300);
    cout << s.pop() << " popped from stack" << endl;
    cout << s.pop() << " popped from stack" << endl;
 
  return 0;
}



#include <iostream>
#include <stack>
#include <string>

using namespace std;

bool isBalanced(string x) {
    stack<char> s;

    for (char ch : x) {
        // If it's an opening bracket, push to stack
        if (ch == '(' || ch == '[' || ch == '{') {
            s.push(ch);
        } 
        // If it's a closing bracket
        else if (ch == ')' || ch == ']' || ch == '}') {
            // Stack empty means no matching opener
            if (s.empty()) return false;

            char top = s.top();
            // Check if the top matches the current closer
            if ((ch == ')' && top == '(') || 
                (ch == ']' && top == '[') || 
                (ch == '}' && top == '{')) {
                s.pop();
            } else {
                return false; // Mismatched pair
            }
        }
    }

    // If stack is empty, all brackets were matched correctly
    return s.empty();
}

int main() {
    string expression = "{[()]}";

    if (isBalanced(expression)) {
        cout << "The expression is accurate (balanced)." << endl;
    } else {
        cout << "The expression is inaccurate (unbalanced)." << endl;
    }

    return 0;
}
