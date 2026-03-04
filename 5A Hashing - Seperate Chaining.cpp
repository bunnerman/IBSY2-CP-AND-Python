#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int n;
	cout << "Enter number of elements: ";
	cin >> n;
	cout << "Enter " << n << " elements: ";
	vector <int> vec;
	for (int i = 0; i < n; i++)
	{
		int t;
		cin >> t;
		vec.push_back(t);
	}

	// Used Hash Function: H(x) = x % 5
	vector <vector <int>> hashTable;
	hashTable.resize(5);
	for (int i = 0; i < n; i++)
	{
		int h = vec[i] % 5;
		hashTable[h].push_back(vec[i]);
	}

	for (int i = 0; i < 5; i++)
	{
		cout << i << ": ";
		for (int j = 0; j < hashTable[i].size(); j++)
			cout << hashTable[i][j] << " ";
		cout << "\n";
	}

	return 0;
}
