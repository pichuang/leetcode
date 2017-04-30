import unittest

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = int(num, 2)
        

class test_Solution(unittest.TestCase):
    
    def test(self):
        s = Solution()
        self.assertEqual(s.findComplement(5), 2)
        self.assertEqual(s.findComplement(1), 0)

if __name__ == '__main__':
    unittest.main()