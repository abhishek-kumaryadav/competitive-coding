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
// #define all(x) (x).begin(), (x).end()~
// #define sz(x) ((ll)(x).size())

int main()
{
    fast_cin();
    ll t;
    cin >> t;
    for (int it = 1; it <= t; it++)
    {
        ll n;
        cin >> n;
        v32 arr(n);
        forn(i, n)
                cin >>
            arr[i];
        int countt = 0;
        set<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
        for (int i = 1; i < pow(2, n); i++)
        {
            // cout << ln << "subset" << i << ln;
            set<int> ma;
            // ordered_set o_set;
            forn(j, n)
            {
                // array element
                int flag = 1;
                // cout << ((i >> j) & 1) << " ";
                if ((i >> j) & 1)
                {
                    // break arr[j] and set in map
                    auto itr = primes.begin();
                    // cout << *itr;
                    int val = arr[j];
                    while (itr != primes.end())
                    {
                        if (val % *itr == 0)
                        {
                            if (ma.find(*itr) == ma.end())
                            {
                                val /= *itr;
                                ma.insert(*itr);
                            }
                            else
                            {
                                flag = 0;
                                ma.clear();
                                break;
                            }
                        }
                        else
                        {
                            itr++;
                        }
                    }
                    if (val != 1)
                    {
                        flag = 0;
                        ma.clear();
                        break;
                    }
                }
                if (!flag)
                {
                    ma.clear();

                    break;
                }
            }
            if (ma.size() != 0)
                countt++;
            // cout << ma.size() << ln;
            // for (auto it : ma)
            // {
            //     cout << it << " ";
            // }
            // cout << ln;
            // ma.clear();
        }
        cout << countt;
    }
    return 0;
}