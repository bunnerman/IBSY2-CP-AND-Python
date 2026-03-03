#include <iostream>
using namespace std;

int main()
{
	int r, c;
	
	cout << "Enter rows x columns: ";
	cin >> r;
	cin >> c;
	int mtrx[r][c];
	cout << "Enter " << r * c << " elements: ";
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			cin >> mtrx[i][j];

	for (int i = 0; i < c; i++)
	{
		for (int j = 0; j < r; j++)
			cout << mtrx[j][i] << " ";
		cout << "\n";
	}
	return 0;
}
