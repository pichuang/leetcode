#!/usr/bin/env python2

import unittest
"""
https://leetcode.com/problems/array-partition-i/#/description

Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4.

Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
"""
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Soring array
        sorted_nums = sorted(nums)
        answer = 0
        for i in range(0, len(sorted_nums), 2):
            answer = answer + int(sorted_nums[i])
        return answer

class test_Solution(unittest.TestCase):
    
    def test(self):
        s = Solution()
        self.assertEqual(s.arrayPairSum([1,4,3,2]), 4)

if __name__ == '__main__':
    unittest.main()