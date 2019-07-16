import unittest
from waimoku import *


class TestWaimoku(unittest.TestCase):
    def test_save_to_file(self):
        waimoku = Waimoku()
        waimoku.save_to_file_from_csv_file(file_path="tests/res/event_132992_participants-3.csv", save_filename="test.xlsx")
