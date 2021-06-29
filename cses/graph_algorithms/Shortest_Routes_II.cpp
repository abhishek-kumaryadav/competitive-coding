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
// #define all(x) (x).begin(), (x).end()
// #define sz(x) ((ll)(x).size())

int main()
{
    fast_cin();
    ll n, m, q;
    cin >> n >> m >> q;
    vector<v64> matt(n + 1, v64(n + 1, INF));
    ll a, b, c;
    forn(i, m)
    {
        cin >> a >> b >> c;
        c = min(c, matt[a][b]);
        matt[a][b] = c;
        matt[b][a] = c;
    }
    forn(i, n) matt[i + 1][i + 1] = 0;
    // cout << matt[1][2];
    // forn(i, n)
    // {
    //     forn(j, n) cout << matt[i + 1][j + 1];
    //     cout << ln;
    // }
    forn(i, n)
    {
        forn(j, n)
        {
            forn(k, n)
            {
                //compare ij and ik kj
                ll su = matt[i + 1][k + 1] + matt[k + 1][j + 1];
                if ((i != j) && (j != k) && (i != k) && !(matt[i + 1][k + 1] == INF) && !(matt[k + 1][j + 1] == INF) && (matt[i + 1][j + 1] > su))
                {
                    matt[i + 1][j + 1] = su;
                    matt[j + 1][i + 1] = su;
                }
            }
        }
    }
    forn(i, q)
    {
        int a, b;
        cin >> a >> b;
        // ll res;
        if (matt[a][b] == INF)
            cout << -1 << ln;
        else
            cout << matt[a][b] << ln;
        // cout << ((matt[a][b] == INF) ? (ll)-1 : matt[a][b]) << ln;
    }
    return 0;
}