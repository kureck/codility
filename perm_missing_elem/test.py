from unittest import main
from unittest import TestCase
from run import solution


class PermMissingElemTest(TestCase):
    def test_1(self):
        '''should return 4'''
        A = [2, 3, 1, 5]
        self.assertEqual(4, solution(A))

    def test_2(self):
        '''should return 3'''
        A = [2, 1, 5, 4]
        self.assertEqual(3, solution(A))

    def test_3(self):
        '''should return 3'''
        A = [2, 1, 5, 4, 8, 6, 3]
        self.assertEqual(7, solution(A))

    def test_empty(self):
        '''should return 1'''
        A = []
        self.assertEqual(1, solution(A))

    def test_single(self):
        '''should return 2'''
        A = [1]
        self.assertEqual(2, solution(A))

if __name__ == '__main__':
    main()
