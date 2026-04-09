#include <iostream>
using namespace std;

int charMap = 256;

bool areAnagram(string &s1, string &s2)
{
	int m = s1.size();
	int n = s2.size();
	if (m != n)
		return false;
	int count[charMap]={0};
	for (int i = 0; i < m ; i++)
	{
		count[s1[i]]++;
		count[s2[i]]--;
	}

	for (int i = 0; i < charMap; i++)
		if (count[i] != 0)
			return false;

	return true;
}

int main()
{
	string s1, s2;
	cin >> s1 >> s2;
	cout << boolalpha << areAnagram(s1, s2);
}
