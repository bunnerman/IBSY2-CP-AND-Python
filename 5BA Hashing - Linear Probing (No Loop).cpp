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
	vector <int> hashTable(5, -1);
	bool hashFull = false;
	for (int i = 0; i < n; i++)
	{
		if (hashFull)
			hashTable.push_back(vec[i]);
		else
		{
			int h = vec[i] % 5;

			if (hashTable[h] == -1)
				hashTable[h] = vec[i];
			else
			{
				while (h < 5 && hashTable[h] != -1)
					h++;
				if (h >= 5)
				{
					hashTable.push_back(vec[i]);
					hashFull = true;
					continue;
				}
				hashTable[h] = vec[i];
			}
		}
	}

	for (int i = 0; i < hashTable.size(); i++)
	{
		cout << i << ": ";
		if (hashTable[i] == -1)
			cout << "---" << "\n";
		else
			cout << hashTable[i] << "\n";
	}

	return 0;
}	
