#include <iostream>
using namespace std;

int main()
{
	int r, c;
	int n;
	
	cout << "Enter rows x columns: ";
	cin >> r;
	cin >> c;
	int mtrx[r][c];
	int tMtrx[c][r];
	cout << "Enter " << r * c << " elements: ";
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
		{
			cin >> mtrx[i][j];
			tMtrx[j][i] = mtrx[i][j];
		}

	for (int i = 0; i < c; i++)
	{
		for (int j = 0; j < r; j++)
			cout << tMtrx[i][j] << " ";
		cout << "\n";
	}
	return 0;
}
