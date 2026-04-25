#include <iostream>
#include <algorithm>
#include <vector>

int main()
{
	int n = 5;
	std::vector<int> vec(n);
	for (int &i: vec)
		std::cin >> i;
	
	for (int i = 0; i < n - 1; i++)
		for (int j = 0; j < n - i - 1; j++)
			if (vec[j] > vec[j + 1])
				std::swap(vec[j], vec[j + 1]);

	for (int &i: vec)
		std::cout << i << " ";
	return 0;
}
