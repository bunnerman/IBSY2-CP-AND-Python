#include <iostream>
using namespace std;

void rec(int N)
{
	if (N == 1)
		cout << "1 ";
	else
	{
		cout << N << " ";
		return rec(N - 1);
	}
}

int main()
{
	int N;
	cout << "Enter N: ";
	cin >> N;
	rec(N);

	return 0;
}
