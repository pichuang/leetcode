import unittest

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class test_Solution(unittest.TestCase):
    
    def test(self):
        s = Solution()
        self.assertEqual(s.reverseString("hello"), "olleh")

if __name__ == '__main__':
    unittest.main()