import context
import objects
import get_grand_prix_names
import datetime
import unittest

class TestGetGrandPrixNames(unittest.TestCase):
    def setUp(self):
        self.grand_prix_names = grand_prix_names = ["Australian", "Chinese", "Bahrain", "Russian", "Spannish", "Monaco", "Canadian", "Azerbaijan", "Austrian", "British", "Hungarian", "Belgian", "Italian", "Singapore", "Malaysian", "Japanese", "United States", "Mexican", "Brazilian", "Abu Dhabi"]

    def tearDown(self):
        self.grand_prix_names = None

    def test_load_all_grands_prix(self):
        grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date(2017,12,31))
        self.assertTrue(len(grand_prix_names) == len(self.grand_prix_names), "Number of Grands Prix read = " + str(len(self.grand_prix_names)))

    def test_first_race(self):
        self.assertEqual(self.grand_prix_names[0], "Australian","First Grand Prix = 'Australian'")

    def test_races_before(self):
        grand_prix_names = get_grand_prix_names.get_grand_prix_names(datetime.date(2017,5,1))
        self.assertTrue(len(grand_prix_names) == 4)

if __name__=='__main__':
    unittest.main(warnings='ignore')
