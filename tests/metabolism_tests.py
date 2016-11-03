import unittest

from anthropometrics.metabolism.metabolism_harris import MetabolismHarris
from anthropometrics.metabolism.metabolism_mifflin import MetabolismMifflin


# todo cambiar nombre de la clase a tests de metabolismo
class MetabolismTests(unittest.TestCase):
    # data tests
    def test_wrong_gender(self):
        with self.assertRaises(ValueError):
            m = MetabolismMifflin(gender=1, activity=1.2, weight=-90, height=180, age=24)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            m = MetabolismMifflin(gender=1, activity=1.2, weight=-90, height=180, age=24)

    def test_negative_weight(self):
        with self.assertRaises(ValueError):
            m = MetabolismMifflin(gender=1, activity=1.2, weight=90, height=-180, age=24)

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            m = MetabolismMifflin(gender=1, activity=1.2, weight=90, height=180, age=-24)

    # mifflin tests
    def test_mifflin_male(self):
        m = MetabolismMifflin(gender=0, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_bmr(), 1915)

    def test_mifflin_male_with_activity(self):
        m = MetabolismMifflin(gender=0, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_tmr(), 2298)

    def test_mifflin_female(self):
        m = MetabolismMifflin(gender=1, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_bmr(), 1749)

    def test_mifflin_female_with_activity(self):
        m = MetabolismMifflin(gender=1, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_tmr(), 2098.7999999999997)

    # harris tests
    def test_harris_male(self):
        m = MetabolismHarris(gender=0, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_bmr(), 2048.715)

    def test_harris_male_with_activity(self):
        m = MetabolismHarris(gender=0, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_tmr(), 2458.458)

    def test_harris_female(self):
        m = MetabolismHarris(gender=1, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_bmr(), 1741.222)

    def test_harris_female_with_activity(self):
        m = MetabolismHarris(gender=1, activity=1.2, weight=90, height=180, age=23)
        self.assertEqual(m.get_tmr(), 2089.4664)

    # TODO hacer tests para embarazo y lactancia
if __name__ == '__main__':
    unittest.main()

