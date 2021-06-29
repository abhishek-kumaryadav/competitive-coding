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
string arr[1001];
vp32 dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
bool vis[1001][1001] = {false};
// vp32 par[1001][1001];
p32 par[1001][1001];
bool isValid(int r, int c)
{
    if (r >= n || r < 0 || c >= m || c < 0)
        return false;
    if (vis[r][c])
        return false;
    if (arr[r][c] == '#')
        return false;
    return true;
}
int main()

{
    fast_cin();
    cin >> n >> m;
    forn(i, n)
            cin >>
        arr[i];

    queue<p32> q;
    bool flag = true;
    p32 start, end;
    for (int i = 0; i < n && flag; i++)
        forn(j, m) if (arr[i][j] == 'A')
        {
            q.push({i, j});
            start.first = i;
            start.second = j;
            par[i][j] = {-1, -1};
            vis[i][j] = true;
            flag = false;
            break;
        }

    // cout << q.front().first << " " << q.front().second << ln;
    // cout << par[1][6].first << " " << par[1][6].second << ln;
    // return 1;
    // q.pu sh({})
    flag = true;
    while (!q.empty() && flag)
    {

        p32 tis = q.front();
        q.pop();
        // cout << tis.first << " " << tis.second << ": ";

        for (auto it : dir)
        {
            int left = tis.first + it.first;
            int right = tis.second + it.second;
            // cout << isValid(3, 6);
            if (isValid(left, right))
            {
                // cout << left << " " << right << "\t";
                par[left][right] = tis;
                vis[left][right] = true;
                q.push({left, right});
                if (arr[left][right] == 'B')
                {
                    flag = false;
                    end.first = left;
                    end.second = right;
                    break;
                }
            }
        }
        // cout << ln;
    }

    // stk.push(start);
    if (flag)
        cout << "NO";
    else
    {
        stack<p32> stk;
        while (end != start)
        {
            stk.push(end);
            end = par[end.first][end.second];
        }
        cout << "YES\n";
        cout << stk.size() << ln;
        p32 prev = start;
        while (!stk.empty())
        {
            p32 it = stk.top();
            stk.pop();
            if (it.first < prev.first)
            {
                cout << "U";
            }
            else if (it.second < prev.second)
            {
                cout << "L";
            }
            else if (it.first > prev.first)
            {
                cout << "D";
            }
            else if (it.second > prev.second)
            {
                cout << "R";
            }
            // cout << it.first << " " << it.second << ln;

            prev = it;
        }
    }
    // cout << par[2][6].first << " " << par[2][6].second;

    return 0;
}