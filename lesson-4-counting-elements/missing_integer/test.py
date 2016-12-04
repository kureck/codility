from unittest import main
from unittest import TestCase
from run import solution


class MissingIntegerTest(TestCase):
    def test_1(self):
        '''should return 5'''

        A = [1, 3, 6, 4, 1, 2]
        self.assertEqual(5, solution(A))

    def test_2(self):
        '''should return 2'''

        A = [1]
        self.assertEqual(2, solution(A))

if __name__ == '__main__':
    main()
