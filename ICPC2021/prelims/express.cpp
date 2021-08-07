#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <queue>
#include <deque>
#define ll long long int
#define ld long double
#define M 1000000007
#define MM 998244353
#define INF 4e18
#define pb push_back
#define bpp __builtin_popcount
#define pii pair<int, int>
#define pll pair<ll, ll>
using namespace std;
#define forn(i, e) for (ll i = 0; i < e; i++)

#define MAX 100000
#define max_val 10000
#define forin(i, start, end) for (int i = start; i < end; i++)
#define count_digit(n) floor(log10(n) + 1)
ll gcd(int a, int b)
{
    return __gcd(a, b);
}

void solve()
{
    ll n, x;
    cin >> n >> x;
    vector<int> arr(32, 0);
    ll t = n;
    int j = 0;
    while (t > 0)
    {
        arr[j] = t % 2;
        j++;
        t = t / 2;
    }
    int count = 0;
    reverse(arr.begin(), arr.end());
    // forn(i, 32)
    // {
    //     cout << arr[i];
    // }
    int flag = 0;
    for (int i = 0; i < 32; i++)
    {
        if (arr[i] == 1)
        {
            if (n <= x)
            {
                count++;
                break;
            }
            else
            {
                if ((31 - i) % 2)
                {
                    count++;
                    n = n ^ (1 << (31 - i));
                }
                else
                {
                    if (!flag && 1 << (31 - i) <= x)
                    {
                        flag = 1;
                        count++;
                        n = n ^ (1 << (31 - i));
                    }
                    else
                    {
                        count += 2;
                        n = n ^ (1 << (31 - i));
                    }
                }
            }
        }
    }
    // cout<<n<< " " <<count <<"\n";
    cout << ((n == 0) ? -1 : count) << "\n";
}

int main()
{
    // #ifndef ONLINE_JUDGE
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
    // #endif
    std::ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t = 1;
    cin >> t;
    while (t-- > 0)
    {
        solve();
    }
    return 0;
}