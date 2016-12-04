from unittest import main
from unittest import TestCase
from run import naive_solution, improved_solution


class OddOccurrencesInArrayTest(TestCase):
    def test_empty_array_naive(self):
        '''should return None'''
        a = []
        self.assertEqual(None, naive_solution(a))

    def test_empty_array_naive(self):
        '''should return None'''
        a = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(7, naive_solution(a))

    def test_empty_array(self):
        '''should return None'''
        a = []
        self.assertEqual(0, improved_solution(a))

    def test_empty_array(self):
        '''should return None'''
        a = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(7, improved_solution(a))

if __name__ == '__main__':
    main()
