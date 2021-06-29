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
int n, m;
int ev = -1, sv = -1;
vector<int> arr[100001];
bool vis[100001] = {false};
int par[100001] = {0};
// v32 color(100001, -1);
// int flag = 0;
bool dfs(int i, int p)
{
    // cout << i << " " << p << ln;
    vis[i] = true;
    par[i] = p;
    // return true;
    for (auto it : arr[i])
    {
        if (it == p)
            continue;
        if (vis[it])
        {

            sv = it;
            ev = i;
            return true;
        }
        else if (dfs(it, i))
            return true;
    }
    return false;
}
int main()
{
    fast_cin();
    cin >> n >> m;
    forn(i, m)
    {
        int a, b;
        cin >> a >> b;
        arr[a].pb(b);
        arr[b].pb(a);
    }
    for (int i = 1; i < n; i++)
    {
        if (!vis[i] && dfs(i, -1))
            break;
    }
    // for (int i = 1; i <= n; i++)
    //     cout << par[i] << " ";
    if (ev == -1)
    {
        cout << "IMPOSSIBLE";
    }
    else
    {
        // int count = 1;
        // cout << sv << " ";
        // int temp = ev;
        v32 pr;
        pr.pb(sv);
        while (ev != sv)
        {
            // cout << ev << " ";
            pr.pb(ev);
            ev = par[ev];
        }
        // cout << sv;
        pr.pb(sv);

        cout << pr.size() << ln;
        for (auto it : pr)
            cout << it << " ";
    }
    return 0;
}