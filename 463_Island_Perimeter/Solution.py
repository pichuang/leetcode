import unittest

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        weight = len(grid[0])
        answer = 0
        for i in range(height):
            for j in range(weight):
                if grid[i][j] == 1:
                    answer += 4
                    if i > 0 and grid[i-1][j] == 1:
                        answer -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        answer -= 2
        return answer

class test_Solution(unittest.TestCase):

    def test(self):
        s = Solution()
        self.assertEqual(s.islandPerimeter([[0, 1, 0, 0],
                                            [1, 1, 1, 0],
                                            [0, 1, 0, 0],
                                            [1, 1, 0, 0]]), 16)

if __name__ == '__main__':
    unittest.main()