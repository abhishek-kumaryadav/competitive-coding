/*
* @Author: abhk943 
* @Date: 2021-05-22 20:20:49 
* @Last Modified by: abhk943
* @Last Modified time: 2021-05-22 20:22:52
*/
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,fma")
#pragma GCC optimize("unroll-loops")
#include "bits/stdc++.h"
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
bool sorr(const pair<int, int> &x, const pair<int, int> &y)
{
    if (x.first == y.first)
        return x.second < y.second;
    return x.first < y.first;
}
// struct range
// {
//     int first;
//     int second;
//     int index;
//     bool operator <(const range &y)const{
//         if(first==y.first)
//             return first<y.
//     }
// };

int main()
{
    fast_cin();
    int n;
    cin >> n;
    vector<pair<pair<int, int>, int>> arr(n);
    forn(i, n)
    {
        cin >> arr[i].first.first >> arr[i].first.second;
        arr[i].second = i;
    }
    sort(all(arr));
    // for (auto it : arr)
    //     cout << it.first.first << " " << it.first.second << " " << it.second << ln;
    int room = 1;
    priority_queue<p32, vp32, greater<p32>> pq;
    v32 assigned(n);
    forn(i, n)
    {
        if (!pq.empty())
        {
            if (arr[i].first.first > pq.top().first)
            {
                p32 temp = pq.top();
                assigned[arr[i].second] = temp.second;
                pq.pop();
                pq.push({arr[i].first.second, temp.second});
            }
            else
            {
                assigned[arr[i].second] = room++;
                pq.push({arr[i].first.second, room - 1});
            }
        }
        else
        {
            assigned[arr[i].second] = room++;
            pq.push({arr[i].first.second, room - 1});
        }
    }
    cout << room - 1 << ln;
    for (auto it : assigned)
        cout << it << " ";
    return 0;
}