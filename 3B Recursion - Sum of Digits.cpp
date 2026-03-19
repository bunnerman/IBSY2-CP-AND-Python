#include <iostream>
using namespace std;

int rec(int N)
{
	if (N == 0)
		return 0;
	else
		return (N % 10) + rec(N / 10);
}

int main()
{
	int N;
	cout << "Enter N: ";
	cin >> N;
	cout << rec(N);
	return 0;
}
