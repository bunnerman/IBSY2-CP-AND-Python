#include <iostream>
using namespace std;

int main()
{
    int N;
    cout << "Enter number of elements: ";
    cin >> N;
	int ary[N];
    cout << "Enter " << N << " elements (ascending order): ";
	for (int &i : ary)
		cin >> i;
	int X; // sum
	cout << "Enter sum: ";
	cin >> X;

	int *a = ary; // ary ≡ &ary[0]
	int *b = &ary[N - 1];
	bool validPair = false;

	while(a < b)
	{
		if (X == *a + *b)
		{
			validPair = true;
			cout << "Valid Pair: " << *a << " & " << *b << "\n";
			a++;
			b--;
		}
		else if (X > *a + *b)
			a++;
		else
			b--;
	}
	if (!validPair)
		cout << "No Valid Pairs";

    return 0;
}
