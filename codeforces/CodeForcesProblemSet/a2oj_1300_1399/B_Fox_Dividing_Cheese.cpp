#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <list>
#include <chrono>
#include <random>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <iomanip>
#include <fstream>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> p32;
typedef pair<ll, ll> p64;
typedef pair<double, double> pdd;
typedef vector<ll> v64;
typedef vector<int> v32;
typedef vector<vector<int>> vv32;
typedef vector<vector<ll>> vv64;
typedef vector<vector<p64>> vvp64;
typedef vector<p64> vp64;
typedef vector<p32> vp32;
ll MOD = 998244353;
double eps = 1e-12;
#define forn(i, e) for (ll i = 0; i < e; i++)
#define forsn(i, s, e) for (ll i = s; i < e; i++)
#define rforn(i, s) for (ll i = s; i >= 0; i--)
#define rforsn(i, s, e) for (ll i = s; i >= e; i--)
#define ln "\n"
#define dbg(x) cout << #x << " = " << x << ln
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define INF 2e18
#define fast_cin()                    \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL)
#define all(x) (x).begin(), (x).end()
#define sz(x) ((ll)(x).size())

ll dfs(ll a, ll b)
{
    // cout << a << " " << b << ln;
    ll out = 0;
    ll zer = 0;
    if (a == b)
        return out;
    if (a > b)
    {
        ll temp = a;
        a = b;
        b = temp;
    }
    ll inff = 1000000000;
    ll temp1 = inff, temp2 = inff, temp3 = inff;
    if (b % 2 == 0)
        temp1 = dfs(a, b / 2);
    if (b % 3 == 0)
        temp2 = dfs(a, b / 3);
    if (b % 5 == 0)
        temp3 = dfs(a, b / 5);
    // cout << temp1 << " " << temp2 << " " << temp3 << ln;
    if ((temp1 == -1 || temp1 == inff) && (temp2 == -1 || temp2 == inff) && (temp3 == -1 || temp3 == inff))
        return -1;
    // else if (temp1 == 1000000000 && temp2 == 1000000000 && temp3 == 1000000000)
    //     return -1;
    else
    {
        ll minna = min(max(zer, temp1), max(zer, temp2));
        minna = min(minna, max(zer, temp3));
        return 1 + minna;
        // return 1 + min(max(zer, temp1), max(zer, temp2));
    }
    // return 1 + min(dfs(a, ));
}
int main()
{
    fast_cin();
    ll a, b;
    cin >> a >> b;
    cout << dfs(a, b);
    return 0;
}