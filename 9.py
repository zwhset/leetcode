# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    回文数

    判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

    :copyright: (c)  2018/12/25 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        return x >= 0 and str(x)[::-1] == str(x)

s = Solution()
print s.isPalindrome(121)
print s.isPalindrome(-121)
print s.isPalindrome(10)
