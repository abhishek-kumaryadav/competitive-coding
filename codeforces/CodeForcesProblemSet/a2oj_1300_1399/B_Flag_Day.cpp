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

int main()
{
    fast_cin();
    int n, m;
    cin >> n >> m;
    // int p1 = {-1,-1}, p2 = {-1,1}, p3 = -1;
    // int arr[3][2] = {{-1, -1}, {-1, -1}, {-1, -1}};
    // set<int> sett;
    map<int, int> mapp;
    // set<int> prev;
    forn(i, m)
    {
        int inp[3];
        // int flag[3] = {};

        set<int> used;
        int flag[3] = {};
        forn(j, 3)
        {
            cin >>
                inp[j];
            if (mapp[inp[j]] != 0)
            {

                flag[j] = 1;
                used.insert(mapp[inp[j]]);
                // setal[mapp[inp[j]] - 1] = 1;
            }
        }
        set<int> allset = {1, 2, 3};
        set<int> unused;
        set_difference(allset.begin(), allset.end(), used.begin(), used.end(), inserter(unused, unused.end()));
        // for (auto j : unused)
        //     cout << j << " ";
        // cout << ln;
        auto itr_unused = unused.begin();
        // cout << (*itr_unused) << (*(++itr_unused));
        forn(j, 3)
        {
            if (flag[j] != 1)
            {
                mapp[inp[j]] = *itr_unused;
                itr_unused++;
            }
        }

        // set<int> colors =
    }
    for (auto i : mapp)
    {
        cout << i.second << " ";
    }

    return 0;
}