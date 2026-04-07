#include <iostream>
#include <algorithm>

int main()
{
	int n = 5;
	std::vector<int> vec(n);
	for (int &i: vec)
		std::cin >> i;
	std::sort(vec.begin(), vec.end());
	for (int &i : vec)
		std::cout << i << " ";

	return 0;
}
