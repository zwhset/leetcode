# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    最长公共前缀

    编写一个函数来查找字符串数组中的最长公共前缀。

    :copyright: (c)  2018/12/25 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        s = strs[0]
        c = ''
        for i in s:
            c += i
            for j in strs[1:]:
                if not j.startswith(c):
                    return c[:-1]
        return c

s = Solution()
print s.longestCommonPrefix(["flower","flow","flight"])
print(s.longestCommonPrefix(["dog","racecar","car"]))
print(s.longestCommonPrefix(["c","c"]))