# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    整数反转

    给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

    :copyright: (c)  2018/12/25 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ri = 0
        if x < 0:
            ri = int('-' + ''.join(reversed(str(x)[1:])))
        else:
            ri = int(''.join(reversed(str(x))))

        if not pow(-2, 31) < ri < (pow(2, 31) - 1):
            return 0
        return ri

s = Solution()
print s.reverse(123)
print s.reverse(-123)
print s.reverse(120)
print s.reverse(1534236469)