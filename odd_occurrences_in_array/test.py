from unittest import main
from unittest import TestCase
from run import solution


class OddOccurrencesInArrayTest(TestCase):
    def test_empty_array(self):
        '''should return None'''
        a = []
        self.assertEqual(None, solution(a))

    def test_empty_array(self):
        '''should return None'''
        a = [9, 3, 9, 3, 9, 7, 9]
        self.assertEqual(7, solution(a))

if __name__ == '__main__':
    main()
