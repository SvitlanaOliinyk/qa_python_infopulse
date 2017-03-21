import unittest
import def_for_hw3_ex2


class TestsDistance(unittest.TestCase):

    def test_zero(self):
        res = def_for_hw3_ex2.distance(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def test_one(self):
        res = def_for_hw3_ex2.distance(0, 0, 0, 1)
        self.assertEqual(res, 1)

    def test_two(self):
        res = def_for_hw3_ex2.distance(0, 0, 1, 1)
        self.assertEqual(res, 2 ** 0.5)

    def test_three(self):
        res = def_for_hw3_ex2.distance(0, 1, 1, 1)
        self.assertEqual(res, 1 ** 0.5)

    def test_four(self):
        res = def_for_hw3_ex2.distance(1, 1, 1, 1)
        self.assertEqual(res, 0 ** 0.5)

    def test_five(self):
        res = def_for_hw3_ex2.distance(4, 5, 1, 1)
        self.assertEqual(res, 25 ** 0.5)


class TestsLeapYear(unittest.TestCase):

    def test_zero(self):
        res = def_for_hw3_ex2.is_year_leap(2016)
        self.assertTrue(res)

    def test_one(self):
        res = def_for_hw3_ex2.is_year_leap(2000)
        self.assertTrue(res)

    def test_two(self):
        res = def_for_hw3_ex2.is_year_leap(0)
        self.assertFalse(res)

    def test_three(self):
        res = def_for_hw3_ex2.is_year_leap(2017)
        self.assertFalse(res)


class TestTriangle(unittest.TestCase):

    def test_zero(self):
        res = def_for_hw3_ex2.is_triangle(1.5,0.5,2)
        self.assertFalse(res)

    def test_one(self):
        res = def_for_hw3_ex2.is_triangle(1.5,2,0.5)
        self.assertFalse(res)

    def test_two(self):
        res = def_for_hw3_ex2.is_triangle(2,0.5,1.5)
        self.assertFalse(res)

    def test_three(self):
        res = def_for_hw3_ex2.is_triangle(3,5,4)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()