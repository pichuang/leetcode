#!/usr/bin/env python2
"""
https://leetcode.com/problems/reshape-the-matrix/#/description
"""
import unittest
import numpy as np

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r(row): int
        :type c(column): int
        :rtype: List[List[int]]
        """

        # http://stackoverflow.com/questions/11264684/flatten-list-of-lists
        # [[1, 2], [3, 4]] -> [1, 2, 3, 4]
        # flattened = [val for sublist in nums for val in sublist]

        try:
            return np.reshape(nums, (r, c)).tolist()
        except:
            return nums

class test_Solution(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.matrixReshape([[1, 2], [3, 4]], r=2, c=4), [[1, 2], [3, 4]])
        self.assertEqual(s.matrixReshape([[1, 2], [3, 4]], r=1, c=4), [[1, 2, 3, 4]])
        self.assertEqual(s.matrixReshape([[1, 2], [3, 4]], r=4, c=1), [[1], [2], [3], [4]])

if __name__ == '__main__':
    unittest.main()