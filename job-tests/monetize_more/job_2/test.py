from unittest import main
from unittest import TestCase
from run import solution


class Job2Test(TestCase):
    def test_1(self):
        '''should return True'''
        A = [1, 5, 3, 3, 7]
        self.assertEqual(True, solution(A))

    def test_2(self):
        '''should return True'''
        A = [1, 5, 3, 1, 7]
        self.assertEqual(True, solution(A))

    def test_3(self):
        '''should return False'''
        A = [1, 5, 3, 1, 1]
        self.assertEqual(False, solution(A))

    def test_4(self):
        '''should return False'''
        A = [1, 1, 1, 1, 1]
        self.assertEqual(False, solution(A))

    def test_5(self):
        '''should return True'''
        A = [2, 1]
        self.assertEqual(True, solution(A))

    def test_6(self):
        '''should return False'''
        A = [1]
        self.assertEqual(False, solution(A))

    def test_7(self):
        '''should return False'''
        A = []
        self.assertEqual(False, solution(A))

    def test_8(self):
        '''should return False'''
        A = [7, 5, 3, 1, 2]
        self.assertEqual(False, solution(A))

    def test_9(self):
        '''should return True'''
        A = [7, 3, 3, 4, 2]
        self.assertEqual(True, solution(A))

    def test_10(self):
        '''should return True'''
        A = [1, 2, 3, 6, 5]
        self.assertEqual(True, solution(A))

if __name__ == '__main__':
    main()
