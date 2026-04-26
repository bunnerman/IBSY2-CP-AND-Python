#include <iostream>
#include <string>
#include <cctype>
#include <stack>
using namespace std;

string infixToPostfix(string str)
{
    stack<char> stk;
    string out;

    for (char ch : str)
    {
        if (ch == 32)
            continue;

        if (isdigit(ch))
            out += ch;
        else if (ch == '(')
            stk.push(ch);
        else if (ch == ')')
        {
            while (stk.top() != '(')
            {
                out += stk.top();
                stk.pop();
            }
            stk.pop();
        }
        else
        {
            while (!stk.empty() &&
                  ((ch == '+' || ch == '-') && (stk.top() == '+' || stk.top() == '-' || stk.top() == '*' || stk.top() == '/')) ||
                  ((ch == '*' || ch == '/') && (stk.top() == '*' || stk.top() == '/')))
            {
                out += stk.top();
                stk.pop();
            }
            stk.push(ch);
        }
    }

    while (!stk.empty())
    {
        out += stk.top();
        stk.pop();
    }

    return out;
}

int main()
{
	string x;
	cout << "Enter string: ";
	getline(cin, x);
	cout << infixToPostfix(x);
}
