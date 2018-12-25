# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c)  2018/12/25 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        Nums = {'C': 100, 'D': 500, 'I': 1, 'L': 50, 'M': 1000, 'V': 5, 'X': 10}
        res = []
        for i, v in enumerate(s):
            try:
                # if v == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                #     res.append(-1)
                #     continue
                # if v == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                #     res.append(-10)
                #     continue
                # if v == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                #     res.append(-100)
                #     continue

                if Nums[v] < Nums[s[i+1]]:
                    res.append(-Nums[v])
                else:
                    res.append(Nums[v])
            except:
                res.append(Nums[v])

        return sum(res)

s = Solution()
print s.romanToInt("III")
print s.romanToInt("IV")
print s.romanToInt("IX")
print s.romanToInt("LVIII")
print s.romanToInt("MCMXCIV")