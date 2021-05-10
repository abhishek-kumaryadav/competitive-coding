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
    vector<pair<int, int>> arr(t);
    map<int, int> mappo;
    set<int> sett;
    map<int, int> mapp;
    // map<int, bool> maat;
    // set<int> setto;
    int count = 0;
    // int tot=0;
    for (int it = 1; it <= t; it++)
    {
        int a, b;
        cin >> a >> b;
        arr[it - 1] = {a, b};

        if (a != b)
        {
            mapp[a]++;
            sett.insert(b);
        }
        else
            mappo[a]++;
        // else
        // {
        // setto.insert(b);
        //     if (sett.find(a) != sett.end())
        // }

        // else if (maat[b] == True)
        //     sett.insert(b);

        // maat[a] = true;
    }
    for (auto i : mappo)
    {
        if (i.second <= 1 && sett.find(i.first) == sett.end())
            count++;
        sett.insert(i.first);
    }
    for (auto i : mapp)
    {
        if (sett.find(i.first) == sett.end())
            count += i.second;
    }

    // cout << mapp.size() << " " << sett.size() << ln;
    // for (auto i : mapp)
    //     cout << i.first << " " << i.second << ln;
    // for (auto i : arr)
    // {
    //     // cout << i.first << i.second << " ";
    //     int minus = 0;
    //     if (i.first == i.second)
    //         minus = 1;
    //     // cout << mapp[i.second];
    //     if (mapp[i.second] - minus > 0)
    //         sett.insert(i.second);
    // }
    // cout << mapp.size() << " " << sett.size() << ln;
    // for (auto i : sett)
    //     mapp.erase(i);
    // int count = 0;
    // // cout << mapp.size() << " " << sett.size() << ln;
    // for (auto i : mapp)
    //     count += i.second;
    cout << count;
    return 0;
}