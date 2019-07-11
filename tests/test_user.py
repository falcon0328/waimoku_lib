import unittest
from datetime import datetime
from waimoku import *


class TestWaimokuUser(unittest.TestCase):
    def test_init(self):
        dummyDateTime = datetime(year=1996, month=3, day=28)
        waimokuUser = WaimokuUser(user_name="aseo",
                                  display_name="瀬尾敦生",
                                  join_status=WaimokuJoinStatus.join,
                                  participation_status=True,
                                  mokumoku="ワイもく！",
                                  is_handagote=True,
                                  is_enquete=True,
                                  is_setsuei=WaimokuSetsueiStatus.all,
                                  is_lt=True,
                                  latest_update=dummyDateTime)
        self.assertEqual(waimokuUser.user_name, "aseo")
        self.assertEqual(waimokuUser.display_name, "瀬尾敦生")
        self.assertEqual(waimokuUser.join_status, WaimokuJoinStatus.join)
        self.assertEqual(waimokuUser.participation_status, True)
        self.assertEqual(waimokuUser.is_enquete, True)
        self.assertEqual(waimokuUser.is_setsuei, WaimokuSetsueiStatus.all)
        self.assertEqual(waimokuUser.is_lt, True)
        self.assertEqual(waimokuUser.latest_update, dummyDateTime)
