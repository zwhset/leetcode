# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    两数之和

    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    :copyright: (c)  2018/12/25 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""

# 暴力法
def two_num_sum(nums, target):

    for i, v in enumerate(nums):
        for j, jv in enumerate(nums[i+1:]):
            if v + jv == target:
                return [i, j + i + 1]
    return []

# HashTable
def two_num_sum_hash(nums, target):
    hash_maps = {}
    for i, v in enumerate(nums):
        hash_maps[v] = i

    for i, v in enumerate(nums):
        com = target - v
        if (com in hash_maps.keys()) and hash_maps.get(com, None) != i:
            return [i, hash_maps.get(com)]

    return []

# Python 独有
def two_num_sum_python(nums, target):
    for i , v in enumerate(nums):
        com = target - v
        if com in nums[i+1:]:
            return [i, nums[i+1:].index(com) + i + 1]
    return []


print two_num_sum([3, 2, 4], 6)
print two_num_sum([2,7,11,15], 9)
print two_num_sum([3, 8, 9, 0, 7], 8)
print two_num_sum([-1,-2,-3,-4,-5], -8)

print('')
print two_num_sum_hash([3, 2, 4], 6)
print two_num_sum_hash([2,7,11,15], 9)
print two_num_sum_hash([3, 8, 9, 0, 7], 8)
print two_num_sum_hash([-1,-2,-3,-4,-5], -8)

print('')
print two_num_sum_python([3, 2, 4], 6)
print two_num_sum_python([2,7,11,15], 9)
print two_num_sum_python([3, 8, 9, 0, 7], 8)
print two_num_sum_python([-1,-2,-3,-4,-5], -8)