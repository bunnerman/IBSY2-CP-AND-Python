#include <iostream>
using namespace std;

class stk
{
	int ary[5]; // change this to change max
	int top = 0; // free top index, not occupied
	public:
	void push(int n)
	{
		if (top >= 5)
		{
			cout << "OFlow\n";
			return;
		}
		ary[top] = n;
		top++;
		cout << "Pushed " << n << "\n";
	}
	void pop()
	{
		if (top == 0)
		{
			cout << "UFlow\n";
			return;
		}
		top--;
		cout << "Popped " << ary[top] << "\n";
	}
	void display()
	{
		for (int i = 0; i < top; i++)
			cout << ary[i] << " ";
		cout << "\n";
	}
};

int main()
{
	stk arr;
	arr.pop();
	arr.push(1);
	arr.push(2);
	arr.push(3);
	arr.push(4);
	arr.push(5);
	arr.push(6);
	arr.pop();
	arr.display();
}

