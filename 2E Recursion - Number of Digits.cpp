#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	long long int P;
	cout << "Enter the value of P: ";
	cin >> P;

	if (P > 0)
		cout << floor(log10(P)) + 1;
	else if (P < 0)
		cout << floor(log10(-P)) + 1;
	else
		cout << "1";
	
	return 0;
}
