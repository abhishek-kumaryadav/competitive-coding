#include <utility>  // for std::pair
#include <vector>   // for std::vector
#include <iostream> // for std::cout & std::endl
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef std::pair<int, int> range;
typedef std::vector<range> rangelist;
#define forn(i, e) for (ll i = 0; i < e; i++)
#define ln "\n"

// function declarations
rangelist findRanges(range targetRange, rangelist candidateRanges);
void print(rangelist list);
int n, m;
range target_range;
rangelist candidate_ranges;
int main()
{
    int tc;
    cin >> tc;
    while (tc--)
    {
        cin >> n >> m;
        target_range = {1, n};
        forn(i, m)
        {
            int tl, tr;
            cin >> tl >> tr;
            candidate_ranges.push_back({tl, tr});
        }
        // range target_range = {1, 4};

        // rangelist candidate_ranges =
        //     {{1, 1}, {2, 3}, {3, 3}};

        rangelist result = findRanges(target_range, candidate_ranges);

        int ans = 0;
        for (auto i : result)
        {
            // cout << i.first << " " << i.second << "\n";
            ans = (ans + (i.second - i.first + 1));
        }
        // cout << "RESULT";
        if (ans == 0)
            cout << "-1\n";
        else
        {
            cout << ans << ln;
        }
    }
    // print(result);
    return 0;
}

// Recursive function that returns the smallest subset of candidateRanges that
// covers the given targetRange.
// If there is no subset that covers the targetRange, then this function
// returns an empty rangelist.
//
rangelist findRanges(range targetRange, rangelist candidateRanges)
{
    rangelist::iterator it;
    rangelist smallest_list_so_far;

    for (it = candidateRanges.begin(); it != candidateRanges.end(); ++it)
    {

        // if this candidate range overlaps the beginning of the target range
        if (it->first <= targetRange.first && it->second >= targetRange.first)
        {

            // if this candidate range also overlaps the end of the target range
            if (it->second >= targetRange.second)
            {

                // done with this level - return a list of ranges consisting only of
                // this single candidate range
                return {*it};
            }
            else
            {
                // prepare new version of targetRange that excludes the subrange
                // overlapped by the present range
                range newTargetRange = {it->second + 1, targetRange.second};

                // prepare new version of candidateRanges that excludes the present range
                // from the list of ranges
                rangelist newCandidateRanges;
                rangelist::iterator it2;
                // copy all ranges up to but not including the present range
                for (it2 = candidateRanges.begin(); it2 != it; ++it2)
                {
                    newCandidateRanges.push_back(*it2);
                }
                // skip the present range
                it2++;
                // copy the remainder of ranges in the list
                for (; it2 != candidateRanges.end(); ++it2)
                {
                    newCandidateRanges.push_back(*it2);
                }

                // recursive call to find the smallest list of ranges that cover the remainder
                // of the target range not covered by the present range
                rangelist subList = findRanges(newTargetRange, newCandidateRanges);

                if (subList.size() == 0)
                {
                    // no solution includes the present range
                    continue;
                }
                else if (smallest_list_so_far.size() == 0 ||           // - first subList that covers the remainder of the target range
                         subList.size() < smallest_list_so_far.size()) // - this subList is smaller than all previous ones checked
                {
                    // add the present range to the subList, which represents a solution
                    // (though possibly not optimal yet) at the present level of recursion
                    subList.push_back(*it);
                    smallest_list_so_far = subList;
                }
            }
        }
    }
    return smallest_list_so_far;
}
