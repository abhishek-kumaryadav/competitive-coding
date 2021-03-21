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

int findIndex(long long arr[], int cur, int n)
{
    for (int i = 0; i < n - 1; i++)
    {
        int index = (cur + i + 1) % n;
        if (arr[index] != 0)
        {
            return arr[index];
        }
    }
    return -1;
}

long long gcd(long long a, long long b)
{
    if (a == 0)
        return b;
    if (b == 0)
        return a;
    if (a == b)
        return a;
    if (a > b)
        return gcd(a - b, b);
    return gcd(a, b - a);
}
// bool solve(long long arr[], int n)
// {
//     ret.clear();
//     int count = 0;
//     int countn = 0;
//     do
//     {
//         count = 0;
//         countn = 0;
//         forn(i, n)
//         {
//             if (arr[i] != 0)
//             {
//                 countn++;
//                 int second = findIndex(arr, i, n); //of next non zero element
//                 if (second == -1)
//                     return true;
//                 else
//                 {
//                     if (gcd(arr[i], arr[second]) == 1)
//                     {
//                         count++;
//                         ret.push_back(arr[second]);
//                         arr[second] = 0; //next non zero element
//                     }
//                 }
//             }
//         }
//     } while (count > 0 && countn != 0);
//     return true;
// }
int main()
{
    fast_cin();
    ll t;
    cin >> t;
    for (int it = 1; it <= t; it++)
    {
        int n;
        cin >> n;
        vector<long long> arr;
        vector<ll> ret;
        forn(i, n)
        {
            long long temp;
            cin >> temp;
            arr.push_back(temp);
        }
        int index = 0;
        int count=0;
        while (arr.size() > 1 || count !=arr.size() )
        {
            int sz = arr.size();
            int first = index % sz;
            int second = (index + 1) % sz;
            count++;
            if (first < second)
            {
                if (gcd(arr[first], arr[second]) == 1)
                {
                    ret.push_back(arr[second]);
                    arr.erase(second);
                    count=0;
                }
            }
            index++;
        }
    }
    return 0;
}