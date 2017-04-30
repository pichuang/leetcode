import unittest

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')

        answer = []
        for word in words:
            lower_word = set(word.lower())
            if lower_word.issubset(line1) or lower_word.issubset(line2) or lower_word.issubset(line3):
                answer.append(word)

        return answer

class test_Solution(unittest.TestCase):
    
    def test(self):
        s = Solution()
        self.assertEqual(s.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])

if __name__ == '__main__':
    unittest.main()