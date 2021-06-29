#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include "bits/stdc++.h"
#include <complex>
#include <queue>
#include <set>
#include <unordered_set>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
template <typename T>
using ordered_set = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
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
// #define aint(x) (x).begin(), (x).end()
// #define sz(x) ((int)(x).size())

vector<vector<pair<ll, ll>>> arr;
// vector<ll> fina;
int main()
{
    fast_cin();
    int n, m;
    cin >> n >> m;
    arr.resize(n + 1);
    // forn(i, n + 1)
    // {
    //     // cout << arr[i].first << " " << arr[i].second << ln;
    //     cout << i << "vector pair" << ln;
    //     for (auto it : arr[i])
    //     {
    //         cout << it.first << it.second << " ";
    //     }
    // }
    // return 0;
    vector<ll> fina(n + 1, (ll)1e18);
    fina[1] = 0;

    forn(i, m)
    {
        ll tl, tr, tw;
        cin >> tl >> tr >> tw;
        arr[tl].push_back({tr, tw});
    }
    // forn(i, n + 1)
    // {
    //     // cout << arr[i].first << " " << arr[i].second << ln;
    //     cout << i << "vector pair" << ln;
    //     for (auto it : arr[i])
    //     {
    //         cout << it.first << it.second << " ";
    //     }
    // }
    // return 0;

    priority_queue<pair<ll, ll>, vector<pair<ll, ll>>, greater<pair<ll, ll>>> q;
    q.push({0, 1});
    while (!q.empty())
    {
        ll first = q.top().second;
        ll wei = q.top().first;
        q.pop();
        if (wei > fina[first])
            continue;
        for (auto it : arr[first])
        {
            ll nex = it.first;
            ll dis = it.second;
            if (fina[nex] <= dis + wei)
                continue;
            else
            {
                fina[nex] = dis + wei;
                // if(q.find({}))
                q.push({fina[nex], nex});
            }
        }
    }
    forn(i, n)
    {
        cout << fina[i + 1] << " ";
    }
    return 0;
}