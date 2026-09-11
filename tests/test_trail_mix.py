import unittest

from trail_mix import servings_possible, total_items


class TrailMixTests(unittest.TestCase):
    def test_total_items(self):
        self.assertEqual(total_items(12, 8, 10), 30)

    def test_servings_possible(self):
        self.assertEqual(servings_possible(30, 5), 6)

    def test_serving_size_must_be_positive(self):
        with self.assertRaises(ValueError):
            servings_possible(30, 0)


if __name__ == "__main__":
    unittest.main()
