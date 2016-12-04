from unittest import main
from unittest import TestCase
from run import solution


class PermCheckTest(TestCase):
    def test_1(self):
        '''should return 1'''
        A = [4, 1, 3, 2]
        self.assertEqual(1, solution(A))

    def test_2(self):
        '''should return 0'''
        A = [4, 1, 3]
        self.assertEqual(0, solution(A))

    def test_3(self):
        '''should return 0'''
        A = [1, 3]
        self.assertEqual(0, solution(A))

    def test_3(self):
        '''should return 0'''
        A = [1, 1]
        self.assertEqual(0, solution(A))

if __name__ == '__main__':
    main()
