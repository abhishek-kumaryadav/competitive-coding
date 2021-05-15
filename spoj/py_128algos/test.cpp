#include <bits/stdc++.h>

using namespace std;

int main()
{
    string s;
    cin >> s;
    int sum = 0;
    for (int i = 0; i < 10; i++)
    {
        // This gives ascii digit for every character
        // 0-9 = 48-57
        // A-z = 65-90
        // a-z = 97-122
        int digit = (int)s[i];

        // Subtract 48 to get actual digit
        digit = digit - 48;
        // Multiply this digit to respective number
        // Index i goes from 0-9
        // We need 1-10 so we will use i+1
        digit = digit * i + 1;
        // Add this to sum
        sum = sum + digit;
    }
    cout << sum;
}