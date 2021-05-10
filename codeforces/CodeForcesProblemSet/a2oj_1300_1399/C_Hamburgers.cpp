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
    string ham;
    cin >> ham;
    ll bb = 0, bs = 0, bc = 0;
    forn(i, ham.size())
    {
        switch (ham[i])
        {
        case 'S':
            bs++;
            break;
        case 'B':
            bb++;
            break;
        case 'C':
            bc++;
            break;

        default:
            break;
        }
    }
    ll nb, ns, nc, pb, ps, pc, r;
    cin >> nb >> ns >> nc;
    cin >> pb >> ps >> pc;
    cin >> r;
    if (bc == 0)
        nc = 0, pc = 0, bc = 1;

    if (bb == 0)
        nb = 0, pb = 0, bb = 1;

    if (bs == 0)
        ns = 0, ps = 0, bs = 1;
    ll count = min(nb / bb, ns / bs);
    count = min(nc / bc, count);
    // cout << count << ln;
    nb -= bb * count;
    ns -= bs * count;
    nc -= bc * count;
    // cout << bb << bs << bc << ln;
    // cout << nb << ns << nc << ln;
    // cout << pb << ps << pc << ln;
    r += nb * pb + ns * ps + nc * pc;
    // cout << r << " " << (pb * bb + ps * bs + pc * bc) << ln;
    count += floor(1.0 * r / (pb * bb + ps * bs + pc * bc));
    cout << count;

    return 0;
}