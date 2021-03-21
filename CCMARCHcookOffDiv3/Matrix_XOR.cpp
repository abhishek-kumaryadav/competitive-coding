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
        int n, m, k;
        cin >> n >> m >> k;
        int xorr = k + 1 + 1;
        // for(int i=1;i<=n;i++)
        //     for(int j=1;j<=m;j++)
        //         xorr=xorr^(k+i+j);
        // xorr=xorr^(2+k);

        // if (m == n)
        // {
        //     for (int i = 1; i <= m; i++)
        //         xorr = xorr ^ (2 * i + k);
        // }
        // else if (m < n)
        // {
        //     for (int i = 1; i <= m; i++)
        //         xorr = xorr ^ (2 * i + k);
        //     for (int i = m + 1; i <= n; i++)
        //     {
        //         for (int j = 1; j <= m; j++)
        //             xorr = xorr ^ (k + i + j);
        //     }
        // }
        // else if (m > n)
        // {
        //     for (int i = 1; i <= n; i++)
        //         xorr = xorr ^ (2 * i + k);
        //     for (int i = n + 1; i <= m; i++)
        //     {
        //         for (int j = 1; j <= n; j++)
        //             xorr = xorr ^ (k + i + j);
        //     }
        // }
         if (m == n)
        {
            for (int i = 1; i <= m; i++)
                xorr = xorr ^ (2 * i + k);
        }
        else if (m < n)
        {
            if(m&1){
                int tempm=m-1;
                tempm=tempm/2;
                for(int i=1;i<=tempm;i++){
                    xorr^=2*i+k;
                    xorr^=2*i+n+k;
                }
                for(int i=1;i<=n;i++)
                    xorr^=i+m+k;
            }else{
                int tempm=m/2;
                for(int i=1;i<=tempm;i++){
                    xorr^=2*i+k;
                    xorr^=2*i+n+k;
                }
            }
        }
        else if (m > n)
        {
            if(n&1){
                int tempn=n-1;
                tempn=tempn/2;
                for(int i=1;i<=tempn;i++){
                    xorr^=2*i+k;
                    xorr^=2*i+m+k;
                }
                for(int i=1;i<=m;i++)
                    xorr^=i+n+k;
            }else{
                int tempn=n/2;
                for(int i=1;i<=tempn;i++){
                    xorr^=2*i+k;
                    xorr^=2*i+m+k;
                }
            }
        }
        xorr = xorr ^ (k + 1 + 1);
        cout << xorr << ln;
    }
    return 0;
}