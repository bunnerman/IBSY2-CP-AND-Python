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

	int max = ary[n - 1];
	cout << "Leaders-\n" << max << "\n";
	for (int i = n-1; i >= 0; i--)
	{
		if (ary[i] > max)
		{
			max = ary[i];
			cout << max << "\n";
		}
	}
	
	return 0;
}
