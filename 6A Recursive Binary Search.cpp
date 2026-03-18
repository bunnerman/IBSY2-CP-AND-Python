#include <iostream> 
using namespace std; 

int recBin(int* ary, int low, int high, int key) 
{ 
	if (low > high) 
		return -1; 
	int mid = (high + low) / 2; 
	if (ary[mid] > key) 
		return recBin(ary, low, mid - 1, key); 
	else if (ary[mid] < key) 
		return recBin(ary, mid + 1, high, key); 
	else 
		return mid; 
} 

int main() 
{ 
	int n; 
	cin >> n; 
	int ary[n]; 
	for (int i = 0; i < n; i++) 
		cin >> ary[i]; 
	int key; 
	cin >> key; 
	
	int result = recBin(ary, 0, n - 1, key); 
	if (result == -1) 
		cout << "Not Present"; 
	else 
		cout << "Index: " << result; 
	return 0; 
}
