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
	bool peakFound = false;

	if (n == 1)
	{
		cout << "Peak found at index 0";
		return 0;
	}
	while (!peakFound) // loop is sure to stop as there is guaranteed to be at least one peak element
	{
		mid = (high + low) / 2;

    // edge case for when mid reaches edge, could be improved upon since when mid reaches edge and n < 2, it is guaranteed to be peak
		if (mid == 0)
			if (ary[0] > ary[1])
				peakFound = true;
			else
				low = mid + 1;
		else if (mid == n - 1)
			if (ary[n - 2] < ary[n - 1])
				peakFound = true;
			else
				high = mid - 1;

    // normal handling
		else if (ary[mid] >= ary[mid + 1])
			if (ary[mid - 1] <= ary[mid])
				peakFound = true;
			else
				high = mid - 1;
		else
			low = mid + 1; 
	}

	cout << "Peak found at index " << mid;

    return 0;
}
