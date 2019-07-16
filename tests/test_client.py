import unittest
from waimoku import *


class TestWaimokuClient(unittest.TestCase):
    waimokuUser1 = WaimokuUser(user_name="aseo1",
                               display_name="falcon0328",
                               full_name="せおあつき",
                               assign="ヤフー株式会社",
                               is_staff="運営枠（各団体の代表）",
                               join_status="参加",
                               participation_status="出席",
                               mokumoku="ワイもく！",
                               is_handagote="はい",
                               is_survey="理解しました",
                               is_setsuei="両方手伝えそう",
                               is_lt="します",
                               latest_update="2019年5月26日 11時04分")
    waimokuUser2 = WaimokuUser(user_name="aseo2",
                               display_name="aseo0328",
                               full_name="せおあつお",
                               assign="ヤフー株式会社",
                               is_staff="一般枠",
                               join_status="参加",
                               participation_status="出席",
                               mokumoku="ワイもく！",
                               is_handagote="はい",
                               is_survey="理解しました",
                               is_setsuei="両方手伝えそう",
                               is_lt="します",
                               latest_update="2019年5月26日 11時04分")
    waimokuUser3 = WaimokuUser(user_name="aseo3",
                               display_name="ase0328",
                               full_name="せおあつし",
                               assign="ヤフー株式会社",
                               is_staff="一般枠",
                               join_status="参加",
                               participation_status="出席",
                               mokumoku="ワイもく！",
                               is_handagote="はい",
                               is_survey="理解しました",
                               is_setsuei="両方手伝えそう",
                               is_lt="します",
                               latest_update="2019年5月26日 11時04分")

    def test_save_to_file(self):
        client = WaimokuClient()
        client.save_to_file([self.waimokuUser1, self.waimokuUser2, self.waimokuUser3])
