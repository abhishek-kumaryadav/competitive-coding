#include <bits/stdc++.h>
using namespace std;
#define all(c) c.begin(), c.end()

int main()
{
	vector<int> v;
	v.push_back(11);
	v.push_back(12);
	v.push_back(13);
	v.push_back(14);
	v.push_back(15);

	// cout << "The last element is: " << *v.rbegin();
	vector<int>
		v2(v.rbegin() + (v.size() / 2), v.rend());
	// prints all the elements
	// cout << "\nThe vector elements in reverse order are:\n";
	sort(all(v2));
	for (auto it = v2.begin(); it != v2.end(); it++)
		cout << *it << " ";
	return 0;
}