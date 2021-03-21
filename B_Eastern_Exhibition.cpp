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

void solve()
{
}
int main()
{
    fast_cin();
    ll t;
    cin >> t;
    for (int it = 1; it <= t; it++)
    {
        int n;  cin>>n;
        ld x=0,y=0;
        forn(i,n){
            ld tx,ty;   cin>>tx>>ty;
            x+=tx;
            y+=ty;
        }
        x/=n;
        y/=n;
        v32 ax;
        v32 ay;
        if(floor(x)==ceil(x)){
            ax.push_back((int)x);
            ax.push_back((int)x-1);
            ax.push_back((int)x+1);
        }else{
            ax.push_back((int)floor(x));
            ax.push_back((int)ceil(x));
        }
        if(floor(y)==ceil(y)){
            ay.push_back((int)y);
            ay.push_back((int)y-1);
            ay.push_back((int)y+1);
        }else{
            ay.push_back((int)floor(y));
            ay.push_back((int)ceil(y));
        }
        int xmin=1e9;
        int xmax=-1*1e9;
        int xcount=0;
        int ycount=0;
        forn(i,ax.size()){
            forn(j,ay.size()){
                if(ax[i])
            }
        }
    }
    return 0;
}