#include <iostream>

using namespace std;

int main()
{
	int n;
	cout << "Enter number of elements: ";
	cin >> n;
	cout << "Enter " << n << " elements: ";
	int ary[n];
	for (int i = 0; i < n; i++)
		cin >> ary[i];

	for (int i = 0; i < n - 1; i++)
	{
		if (ary[i] > ary[i + 1])
		{
			cout << "Unsorted List";
			return 0; 
		}
	}

	cout << "Sorted List";

	return 0;		
}
