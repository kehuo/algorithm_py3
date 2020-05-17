# @File: 1
# @Author: Kevin Huo
# @LastUpdate: 5/17/2020 12:47 AM

"""
https://leetcode-cn.com/contest/weekly-contest-189/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
"""

from typing import List


class Solution:
    def peopleIndexes_v1(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = set()

        new_f = []
        for x in favoriteCompanies:
            new_f.append(set(x))

        f = new_f
        n = len(f)
        for i in range(n):
            sub = False
            for j in range(n):
                if i == j:
                    continue
                else:
                    # set([1, 2]) | set([2, 3]) = {1, 2, 3}
                    if f[i] | f[j] == f[j]:
                        # res.add(j)
                        sub = True
                        break
            if not sub:
                res.add(i)

        return sorted(list(res))


