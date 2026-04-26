#include <iostream>
#include <string>
#include <stack>
using namespace std;

bool paraChecker(string str) // checks for order and pairing of () and []
{
	stack <char> stk;

	for (char ch : str)
    {
        if (ch == '(' || ch == '[')
            stk.push(ch);
        else if (ch == ')' || ch == ']')
        {
            if (stk.empty())
                return false;
            if ((ch == ')' && stk.top() != '(') || (ch == ']' && stk.top() != '['))
                return false;
            stk.pop();
        }
    }

	return stk.empty();
}

int main()
{
	string x;
	cout << "Enter string: ";
	getline(cin, x);
	paraChecker(x) ? cout << "YES" : cout << "NO";
}
