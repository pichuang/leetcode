import unittest

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        answer = 0
        for num in nums:
            if num == 1:
                temp += 1
                answer = max(answer, temp)
            elif num == 0:
                temp = 0
        return answer

class test_Solution(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.findMaxConsecutiveOnes([1,1,0,1,1,1]), 3)

if __name__ == '__main__':
    unittest.main()