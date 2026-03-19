#include <iostream>
#include <cmath>
using namespace std;

long long int fac(long long int n)
{
	if (n == 1)
		return 1;
	else
		return n * fac(n - 1);
}

int main()
{
	int P;
	cout << "Enter the value of P: ";
	cin >> P;

	auto ftrl = fac(P);
	cout << floor(log10(ftrl)) + 1;

}
