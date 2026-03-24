#include <iostream>
using namespace std;

int main()
{
    int n;
    cout << "Enter number of elements: ";
    cin >> n;
	int ary[n];
    cout << "Enter " << n << " elements: ";
	for (int &i : ary)
		cin >> i;

	int low = 0;
	int high = n - 1;
	int mid;

	while (1) // loop is sure to stop as there is guaranteed to be at least one peak element
	{
		mid = (high + low) / 2;

		if ((mid == 0 || ary[mid - 1] <= ary[mid]) && (mid == n - 1 || ary[mid] >= ary[mid + 1]))
			break;
		else if (ary[mid - 1] > ary[mid])
			high = mid - 1;
		else
			low = mid + 1;
	}

	cout << "Peak found at index " << mid;

    return 0;
}
