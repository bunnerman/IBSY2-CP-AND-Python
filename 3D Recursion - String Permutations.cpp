#include <iostream>
#include <string>
using namespace std;

void nPrStringRecursive(string *s, int l, int r) 
{
    if (l == r) 
	{
        cout << *s << "\n";
        return;
    }
    for (int i = l; i <= r; i++) 
	{
        swap((*s)[l], (*s)[i]);
        nPrStringRecursive(s, l + 1, r);
		swap((*s)[l], (*s)[i]);
    }
}

int main()
{
	string customStr;
	cout << "Enter string: ";
	cin >> customStr;
	nPrStringRecursive(&customStr, 0, customStr.length() - 1);
}
