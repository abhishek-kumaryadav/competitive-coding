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
vector<int> arr[100001];
bool vis[100001] = {false};
// int dist[100001] = {};
int par[100001] = {0};
// string path = "1";
// vector<int> path;
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
    // int s = bfs(1);
    queue<int> q;
    vis[1] = true;
    q.push(1);
    // dist[1] = 1;
    par[1] = -1;
    // path.pb(1);
    bool flag = true;
    while (!q.empty() && flag)
    {
        int top = q.front();

        // cout << top << ln;

        q.pop();
        // path.pb(top);
        for (auto u : arr[top])
        {

            if (vis[u])
                continue;
            par[u] = top;
            vis[u] = true;

            // dist[u] = dist[top] + 1;
            q.push(u);
            if (u == n)
            {
                flag = false;
                break;
            }
        }
        // path.pop_back();
    }

    if (vis[n])
    {
        int sv = 1, ev = n;
        // v32 path;
        stack<int> stk;
        while (ev != sv)
        {
            // cout << ev << " ";
            // path.insert(path.begin(), ev);
            stk.push(ev);
            ev = par[ev];
        }
        // path.insert(path.begin(), sv);
        stk.push(sv);
        cout << stk.size() << ln;
        // for (auto it : path)
        // {
        //     cout << it << " ";
        // }
        while (!stk.empty())
        {
            cout << stk.top() << " ";
            stk.pop();
        }
        // cout << dist[n] << ln;
        // for (auto it : path)
        //     cout << it << " ";
    }
    else
        cout << "IMPOSSIBLE";

    // forn(i, n)
    // {
    //     for (auto it : arr[i])
    //         cout << it << " ";
    //     cout << ln;
    // }
    return 0;
}