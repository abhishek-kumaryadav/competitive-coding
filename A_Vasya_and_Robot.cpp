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
int n, l, r, Ql, Qr;
map<pair<int,int>,int> ma;
int collectItems(int flag,int arr[], int lt, int rt)
{
    if(ma.count({lt,rt})!=0)
        return ma[{lt,rt}];
    if(lt>rt){
        return 0;
    }else{
        if(flag==0){    // Left
            int left=(arr[lt]*l+Ql+collectItems(0,arr,lt+1,rt));
            int right=(arr[rt]*r+collectItems(1,arr,lt,rt-1));
            if(left<=right){
                if(ma.count({lt,rt})==0)
                    ma.insert({{lt,rt},left});
                return left;
            }else{
                if(ma.count({lt,rt})==0)
                    ma.insert({{lt,rt},right});
                return right;
            }
        }else{      // Right
            int left=(arr[lt]*l+collectItems(0,arr,lt+1,rt));
            int right=(arr[rt]*r+Qr+collectItems(1,arr,lt,rt-1));
            if(left<=right){
                if(ma.count({lt,rt})==0)
                    ma.insert({{lt,rt},left});
                return left;
            }else{
                if(ma.count({lt,rt})==0)
                    ma.insert({{lt,rt},right});
                return right;
            }
        }
    }
}
int main()
{
    fast_cin();

    
    cin >> n >> l >> r >> Ql >> Qr;
    int arr[n];
    forn(i, n)
            cin >>arr[i];
    
    int retval=min((arr[0]*l+collectItems(0,arr,1,n-1)),(arr[n-1]*r+collectItems(1,arr,0,n-2)));
    cout<<retval<<ln;
    return 0;
}