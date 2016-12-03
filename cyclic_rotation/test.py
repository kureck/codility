from unittest import main
from unittest import TestCase
from run import solution


class CyclicRotationTest(TestCase):
    def test_empty_array(self):
        '''should return []'''
        k = 3
        a = []
        self.assertEqual([], solution(a, k))

    def test_K_e_zero(self):
        '''should return [3, 8, 9, 7, 6]'''
        k = 0
        a = [3, 8, 9, 7, 6]
        self.assertEqual([3, 8, 9, 7, 6], solution(a, k))

    def test_K_lt_A(self):
        '''should return [9, 7, 6, 3, 8]'''
        k = 3
        a = [3, 8, 9, 7, 6]
        self.assertEqual([9, 7, 6, 3, 8], solution(a, k))

    def test_K_gt_A(self):
        '''should return [7, 6, 3, 8, 9]'''
        k = 7
        a = [3, 8, 9, 7, 6]
        self.assertEqual([7, 6, 3, 8, 9], solution(a, k))

    def test_array_small_k(self):
        '''should return  [6, 7, 1, 2, 3, 4, 5]'''
        k = 2
        a = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual([6, 7, 1, 2, 3, 4, 5], solution(a, k))

    def test_array_big_k(self):
        '''should return  [3, 5, 1, 1, 2]'''
        k = 12
        a = [1, 1, 2, 3, 5]
        self.assertEqual([3, 5, 1, 1, 2], solution(a, k))

if __name__ == '__main__':
    main()
