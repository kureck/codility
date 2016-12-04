from unittest import main
from unittest import TestCase
from run import solution2


class MaxCountersTest(TestCase):
    def test_1(self):
        '''should return [3, 2, 2, 4, 2]'''
        N = 5
        A = [3, 4, 4, 6, 1, 4, 4]

        self.assertEqual([3, 2, 2, 4, 2], solution2(N, A))

if __name__ == '__main__':
    main()
