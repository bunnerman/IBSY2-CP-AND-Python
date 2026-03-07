#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	cout << "Enter number of elements: ";
	cin >> n;
	cout << "Enter " << n << " elements: ";
	vector <int> vec(n);
	for (int i = 0; i < n; i++)
		cin >> vec[i];

	// Used Hash Function: H(x) = x % 5
	vector <vector <int>> hashTable(5);
	for (int i = 0; i < n; i++)
	{
		int h = vec[i] % 5;
		hashTable[h].push_back(vec[i]);
	}

	for (int i = 0; i < 5; i++)
	{
		cout << i << ": ";
		for (int element : hashTable[i])
			cout << element << " ";
		cout << "\n";
	}

	return 0;
}
