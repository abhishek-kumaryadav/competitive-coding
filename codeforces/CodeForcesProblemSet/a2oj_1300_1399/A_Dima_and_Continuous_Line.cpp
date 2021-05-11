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
    int n;
    cin >> n;
    int arr[n];
    forn(i, n)
            cin >>
        arr[i];
    int first = arr[0];
    int left = -1 * (int)1e7, right = (int)1e7;

    // int right = arr[1];
    int flag = 1;

    // int i = 2;
    // if (left<right){

    // }
    // int closeleft = -1 * (int)1e7, closeright = (int)1e7, farleft = arr[0], farright = arr[0];
    int i = 1;
    while (i < n)
    {
        if ()
    }

    //     i++;
    // }
    // if (left < right)
    // {
    //     int i = 2;
    //     while (i < n)
    //     {
    //         if (arr[i]>=right)
    //         {
    //             /* code */
    //         }

    //         i++;
    //     }
    // }
    // if (left < right)
    // {
    //     int i = 2;
    //     while (i < n - 1)
    //     {
    //         if (arr[i] >= left && arr[i] <= arr[i + 1] && arr[i + 1] <= right)
    //         {
    //             left = arr[i];
    //             right = arr[i + 1];
    //         }
    //         else
    //         {
    //             flag = 0;
    //             break;
    //         }
    //         i += 2;
    //     }
    //     if (i == n - 1 && (arr[i] < left || arr[i] > right))
    //         flag = 0;
    // }
    // else
    // {
    //     int i = 2;
    //     while (i < n - 1)
    //     {
    //         if (arr[i] <= right && arr[i] >= arr[i + 1] && arr[i + 1] >= left)
    //         {
    //             right = arr[i];
    //             left = arr[i + 1];
    //         }
    //         else
    //         {
    //             flag = 0;
    //             break;
    //         }
    //         i += 2;
    //     }
    //     if (i == n - 1 && (arr[i] < left || arr[i] > right))
    //         flag = 0;
    // }
    cout << (flag ? "no" : "yes");
    return 0;
}