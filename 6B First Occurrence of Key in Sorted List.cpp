#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter " << n << " elements (ascending order): ";
    int ary[n];
    for (int i = 0; i < n; i++)
        cin >> ary[i];

	int key;
	cout << "Enter key: ";
	cin >> key;

	int low = 0, high = n - 1;
	int mid;
	bool keyFound = false;
	int first;

	while (high >= low)
	{
		mid = (high + low) / 2;
		if (key == ary[mid])
		{
			keyFound = true;
			first = mid; // assume this is the only element until u find more
			high = mid - 1; // search left binararily, avoid turning it into linear complexity, assume worst case - many occurrences are present instead of just 1 or 2, if not, just linearly search backwards until you find the first occurrence
		}
		else if (key > ary[mid])
			low = mid + 1;
		else
			high = mid - 1;
	}

	if (!keyFound)
		cout << "Key not present";
	else
		cout << "First occurrence found at index " << first;

    return 0;
}
