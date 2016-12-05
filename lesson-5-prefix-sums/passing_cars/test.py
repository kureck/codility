from unittest import main
from unittest import TestCase
from run import solution


class PassingCarsTest(TestCase):
    def test_1(self):
        '''should return 5'''
        A = [0, 1, 0, 1, 1]
        self.assertEqual(5, solution(A))

if __name__ == '__main__':
    main()
