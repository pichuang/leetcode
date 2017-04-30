#!/usr/bin/env python2

import unittest
"""

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 2^31

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count("1")

class test_Solution(unittest.TestCase):
    
    def test(self):
        s = Solution()
        #0010, 1010
        self.assertEqual(s.hammingDistance(x=2, y=10), 1)

        #0001, 0100
        self.assertEqual(s.hammingDistance(x=1, y=4), 2)
        self.assertEqual(s.hammingDistance(x=1, y=0), 1)
        self.assertEqual(s.hammingDistance(x=1, y=1), 0)

        #1011101, 1001001
        self.assertEqual(s.hammingDistance(x=93, y=73), 2)

if __name__ == '__main__':
    unittest.main()
