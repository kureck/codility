from unittest import main
from unittest import TestCase
from run import solution


class Job1Test(TestCase):
    def test_1(self):
        '''should return 4'''
        A = [1, 4, -1, 3, 2]
        self.assertEqual(4, solution(A))

    def test_empty(self):
        '''should return 0'''
        A = []
        self.assertEqual(0, solution(A))

    def test_minus_1(self):
        '''should return 1'''
        A = [-1]
        self.assertEqual(1, solution(A))

    def test_1_item_in_list(self):
        '''should return 1'''
        A = [0, -1]
        self.assertEqual(1, solution(A))

    def test_9_items(self):
        '''should return 10'''
        A = [1, 2, 3, 4, 5, 6, 7, 8, -1]
        self.assertEqual(9, solution(A))

if __name__ == '__main__':
    main()
