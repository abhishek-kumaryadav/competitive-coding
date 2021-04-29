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
    ll t;
    cin >> t;
    for (int it = 1; it <= t; it++)
    {
        int n;
        cin >> n;
        v32 uni;
        // v32 str;
        set<int> sett;
        forn(i, n)
        {
            int temp;
            cin >> temp;
            sett.insert(temp);
            uni.pb(temp);
        }
        map<int, vector<int>> mapp;
        forn(i, n)
        {
            int temp;
            cin >> temp;
            mapp[uni[i]].pb(temp);
        }
        for (auto itr = sett.begin(); itr != sett.end(); itr++)
        {
            sort(mapp[*itr].begin(), mapp[*itr].end(), greater<int>());
            // cout << *itr << " ";
        }
        for (auto itr = sett.begin(); itr != sett.end(); itr++)
        {
            int prev = 0;
            int sz = mapp[*itr].size();
            forn(j, sz)
            {
                int temp = mapp[*itr][j];
                mapp[*itr][j] += prev;
                prev = mapp[*itr][j];
            }
        }
        for (int i = 1; i <= n; i++)
        {
            int out = 0;
            for (auto itr = sett.begin(); itr != sett.end(); itr++)
            {
                if (mapp[*itr].size() >= i)
                {
                    int size = (mapp[*itr].size() / i) * i;
                    // cout << ln << size << ln;
                    // for (int j = 0; j < size; j++)
                    // {
                    //     out += mapp[*itr][j];
                    // }
                    out += mapp[*itr][size - 1];
                }
            }
            cout << out << " ";
        }
        cout << ln;
    }
    return 0;
}