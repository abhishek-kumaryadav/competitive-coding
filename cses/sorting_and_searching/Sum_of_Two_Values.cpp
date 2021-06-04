/*
* @Author: abhk943 
* @Date: 2021-05-22 20:20:49 
* @Last Modified by: abhk943
* @Last Modified time: 2021-05-22 20:22:52
*/
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

int main()
{
    fast_cin();
    int n, x;
    cin >> n >> x;
    vector<pair<int, int>> vec(n);
    forn(i, n)
    {
        int temp;
        cin >> temp;
        vec[i] = {temp, i + 1};
    }
    int i = 0, j = n - 1;
    sort(all(vec));
    while (i < j)
    {
        int sum = vec[i].first + vec[j].first;
        // cout << i << " " << j << " " << sum << "\n";
        if (sum == x)
        {
            cout << vec[i].second << " " << vec[j].second;
            return 0;
        }
        else if (sum > x)
            j--;
        else
            i++;
    }
    cout << "IMPOSSIBLE";
    // unordered_set<int> sett(all(vec));
    // bool flag = false;
    // forn(i, n)
    // {
    //     auto t = sett.find(x - vec[i]);
    //     if (t != sett.end())
    //     {
    //         flag = true;
    //         cout << i + 1 << " " << vec.find(x - vec[i]) - vec.begin() + 1;
    //         break;
    //     }
    // }
    // if (!flag)
    //     cout << "IMPOSSIBLE";
    return 0;
}