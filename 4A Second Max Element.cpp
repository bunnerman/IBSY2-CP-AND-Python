#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

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
	
	int max = ary[0];
	int max2 = ary[1]; // second max

	for (int i = 0; i < n; i++)
	{
		if (ary[i] > max)
		{
			max2 = max;
			max = ary[i];
		}
		else if (ary[i] < max && ary[i] > max2)
			max2 = ary[i];
	}

	cout << "Max: " << max << "\n";
	cout << "2nd max: " << max2;

	return 0;		
}
