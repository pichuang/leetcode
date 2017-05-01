import unittest

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n%4 != 0)

class test_Solution(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertTrue(s.canWinNim(4), False)

if __name__ == '__main__':
    unittest.main()