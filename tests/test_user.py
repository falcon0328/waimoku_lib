import unittest
from datetime import datetime
from waimoku import *


class TestWaimokuUser(unittest.TestCase):
    def test_init(self):
        dummyDateTime = datetime(year=2019, month=5, day=26, hour=11, minute=4)
        waimokuUser = WaimokuUser(user_name="aseo",
                                  display_name="瀬尾敦生",
                                  join_status="参加",
                                  participation_status="出席",
                                  mokumoku="ワイもく！",
                                  is_handagote="はい",
                                  is_survey="理解しました",
                                  is_setsuei="両方手伝えそう",
                                  is_lt="します",
                                  latest_update="2019年5月26日 11時04分")
        self.assertEqual(waimokuUser.user_name, "aseo")
        self.assertEqual(waimokuUser.display_name, "瀬尾敦生")
        self.assertEqual(waimokuUser.join_status, True)
        self.assertEqual(waimokuUser.participation_status, True)
        self.assertEqual(waimokuUser.mokumoku, "ワイもく！")
        self.assertEqual(waimokuUser.is_handagote, True)
        self.assertEqual(waimokuUser.is_survey, True)
        self.assertEqual(waimokuUser.is_setsuei, WaimokuSetsueiStatus.all)
        self.assertEqual(waimokuUser.is_lt, True)
        self.assertEqual(waimokuUser.latest_update, dummyDateTime)
