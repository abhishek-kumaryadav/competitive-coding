
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include "bits/stdc++.h"
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
#define tr(container, it) for (typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define present(container, element) (container.find(element) != container.end())
#define cpresent(container, element) (find(all(container), element) != container.end())
#define all(c) c.begin(), c.end()
#define sz(c) c.size()
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
// #define all(x) (x).begin(), (x).end()
// #define sz(x) ((ll)(x).size())
struct ranges
{
    int first;
    int second;
    int index;
    bool operator<(const ranges &y) const
    {
        if (first == y.first)
            return second > y.second;
        return first < y.first;
    }
};
// int x=0,y=1;
// swap(x,y);
// bool comapre(p32 x, p32 y)
// {
//     if (x.first == y.first)
//         return x.second > y.second;
//     return x.first < y.first;
// }

int main()
{
    fast_cin();
    int n;
    cin >> n;
    // vp32 arr(n);
    struct ranges arr[n];
    forn(i, n)
    {
        cin >>
            arr[i].first >> arr[i].second;
        arr[i].index = i;
    }
    sort(arr, arr + n);
    // for (auto it : arr)
    //     cout
    //         << it.first << " " << it.second << ln;
    int ma = 0;
    v32 contains(n, 0);
    v32 contained(n, 0);
    forn(i, n)
    {
        if (arr[i].second <= ma)
            contained[arr[i].index] = 1;
        ma = max(ma, arr[i].second);
    }
    ma = (int)1e9;
    for (int i = n - 1; i >= 0; i--)
    {
        if (arr[i].second >= ma)
            contains[arr[i].index] = 1;
        ma = min(ma, arr[i].second);
    }
    for (auto it : contains)
        cout
            << it << " ";
    cout << ln;
    for (auto it : contained)
        cout
            << it << " ";
    return 0;
}