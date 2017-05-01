import unittest

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []

        for num in nums:
            

        return answer

class test_Solution(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.nextGreaterElement(findNums=[4, 1, 2], nums=[1, 3, 4, 2]), [-1, 3, -1])
        self.assertEqual(s.nextGreaterElement(findNums=[2, 4], nums=[1, 2, 3, 4]), [3, -1])


if __name__ == '__main__':
    unittest.main()