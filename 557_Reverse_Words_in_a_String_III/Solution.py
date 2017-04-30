import unittest
"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        return ' '.join(i[::-1] for i in s.split())

class test_Solution(unittest.TestCase):
    
    def test(self):
        s = Solution()
        self.assertEqual(s.reverseWords("Let's take LeetCode contest"), "s'teL ekat edoCteeL tsetnoc")

if __name__ == '__main__':
    unittest.main()