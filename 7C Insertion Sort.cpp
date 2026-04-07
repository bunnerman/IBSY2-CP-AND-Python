#include <iostream>
#include <algorithm>

int main()
{
	int n = 5;
	std::vector<int> vec(n);
	for (int &i: vec)
		std::cin >> i;
	
	for (int i = 1; i < n; i++)
	{
		int j = i - 1;
		int t = vec[i];
		while (j >= 0 && vec[j] > t)
		{
			vec[j + 1] = vec[j];
			j--;
		}
		vec[j + 1] = t;
	}
	for (int &i: vec)
		std::cout << i << " ";
	return 0;
}
