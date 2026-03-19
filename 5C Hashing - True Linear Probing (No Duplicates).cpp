#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter " << n << " elements (NO DUPLICATES): ";
    vector<int> vec(n);
    for (int i = 0; i < n; i++)
        cin >> vec[i];

    int size;
	cout << "Enter size of hash table (H(x) = x \% size): ";
	cin >> size;
    vector<int> hashTable(size, -1);

    for (int i = 0; i < n; i++)
    {
        int value = vec[i];
        int h = value % size;
        int loopDetectVar = h;

        while (hashTable[h] != -1)
        {
            h = (h + 1) % size;
            if (h == loopDetectVar)
                break;
        }
        if (hashTable[h] == -1)
            hashTable[h] = value;
        else
            cout << "HASH TABLE FULL, " << value << " NOT INSERTED\n";
    }

    for (int i = 0; i < size; i++)
    {
        cout << i << ": ";
        if (hashTable[i] == -1)
            cout << "---" << "\n";
        else
            cout << hashTable[i] << "\n";
    }

    return 0;
}
