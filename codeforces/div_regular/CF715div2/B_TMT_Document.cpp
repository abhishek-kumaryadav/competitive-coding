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
        v32 arr;
        int numm = 0;
        v32 arrm;
        forn(i, n)
        {
            char temp;
            cin >> temp;
            int a = int(temp);
            if (a == 77)
                numm++;
            arrm.pb(numm);
            arr.pb(a);
        }
        // # 84:T 77:M
        int ms = n / 3;
        if (numm == ms)
        {
            int i = 0, j = n - 1;
            int flag = 0;
            while (i < j && !flag)
            {
                while (arr[i] == 77)
                    i++;
                while (arr[j] == 77)
                    j--;
                if (i < j)
                {
                    if (arrm[j] - arrm[i] >= ms)
                        ms--;
                    else
                        flag = 1;
                }
                i++;
                j--;
            }
            cout << (flag ? "NO\n" : "YES\n");
        }
        else
        {
            cout << "NO\n";
        }
        // forn(i, n)
        //         cout
        //     << arr[i] << arrm[i];
        // cout << ln;
    }
    return 0;
}