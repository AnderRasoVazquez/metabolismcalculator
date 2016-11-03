import unittest

from anthropometrics.anthropometrics import Metabolism

# todo cambiar nombre de la clase a tests de metabolismo
class AnthropometricTests(unittest.TestCase):
    # data tests
    # TODO refactor quitar estos tests y ponerlos en otro archivo
    def test_bmi(self):
        m = Metabolism(0, 90, 180, 23)
        self.assertEqual(m.get_bmi(), 27.777777777777775)

    def test_whr(self):
        m = Metabolism(gender=0, waist_circumference=111, hip_circumference=107)
        self.assertEqual(m.get_whr(), 1.0373831775700935)

    def test_whr_male_high_risk_true(self):
        m = Metabolism(gender=0, waist_circumference=111, hip_circumference=107)
        self.assertTrue(m.has_whr_risk())

    def test_whr_female_high_risk_true(self):
        m = Metabolism(gender=1, waist_circumference=106, hip_circumference=107)
        self.assertTrue(m.has_whr_risk())

    def test_whr_male_high_risk_false(self):
        m = Metabolism(gender=0, waist_circumference=106, hip_circumference=107)
        self.assertFalse(m.has_whr_risk())

    def test_whr_female_high_risk_false(self):
        m = Metabolism(gender=1, waist_circumference=88, hip_circumference=107)
        self.assertFalse(m.has_whr_risk())

    def test_complexion_male_ectomorf(self):
        m = Metabolism(gender=1, wrist_circumference=16, height=180)
        self.assertEqual(m.get_complexion(), 0)

    def test_complexion_male_mesomorf(self):
        m = Metabolism(gender=1, wrist_circumference=18, height=180)
        self.assertEqual(m.get_complexion(), 1)

    def test_complexion_male_endomorf(self):
        m = Metabolism(gender=1, wrist_circumference=19, height=180)
        self.assertEqual(m.get_complexion(), 2)

    def test_complexion_female_ectomorf(self):
        m = Metabolism(gender=1, wrist_circumference=13, height=145)
        self.assertEqual(m.get_complexion(), 0)

    def test_complexion_female_mesomorf(self):
        m = Metabolism(gender=1, wrist_circumference=14, height=145)
        self.assertEqual(m.get_complexion(), 1)

    def test_complexion_female_endomorf(self):
        m = Metabolism(gender=1, wrist_circumference=15, height=145)
        self.assertEqual(m.get_complexion(), 2)

    def test_ideal_body_weight_devine_male(self):
        m = Metabolism(gender=0, height=180)
        self.assertEqual(m.get_ideal_body_weight_devine(), 75.116)

    def test_ideal_body_weight_devine_female(self):
        m = Metabolism(gender=1, height=145)
        self.assertEqual(m.get_ideal_body_weight_devine(), 38.76599999999999)

    def test_ideal_body_weight_robinson_male(self):
        m = Metabolism(gender=0, height=180)
        self.assertEqual(m.get_ideal_body_weight_robinson(), 72.6448)

    def test_ideal_body_weight_robinson_female(self):
        m = Metabolism(gender=1, height=145)
        self.assertEqual(m.get_ideal_body_weight_robinson(), 44.0494)

    def test_ideal_body_weight_miller_male(self):
        m = Metabolism(gender=0, height=180)
        self.assertEqual(m.get_ideal_body_weight_miller(), 71.518)

    def test_ideal_body_weight_miller_female(self):
        m = Metabolism(gender=1, height=145)
        self.assertEqual(m.get_ideal_body_weight_miller(), 49.13804)

    def test_ideal_body_weight_hamwi_male(self):
        m = Metabolism(gender=0, height=180)
        self.assertEqual(m.get_ideal_body_weight_hamwi(), 77.5388)

    def test_ideal_body_weight_hamwi_female(self):
        m = Metabolism(gender=1, height=145)
        self.assertEqual(m.get_ideal_body_weight_hamwi(), 39.09159999999999)

    def test_ideal_body_weight_lemmens_male(self):
        m = Metabolism(gender=0, height=180)
        self.assertEqual(m.get_ideal_body_weight_lemmens(), 71.28)

    def test_ideal_body_weight_lemmens_female(self):
        m = Metabolism(gender=1, height=145)
        self.assertEqual(m.get_ideal_body_weight_lemmens(), 46.255)

    def test_ideal_body_weight_media_male(self):
        m = Metabolism(gender=0, height=180)
        self.assertEqual(m.get_ideal_body_weight_average(), 73.61952000000001)

    def test_ideal_body_weight_media_female(self):
        m = Metabolism(gender=1, height=145)
        self.assertEqual(m.get_ideal_body_weight_average(), 43.460007999999995)

if __name__ == '__main__':
    unittest.main()
