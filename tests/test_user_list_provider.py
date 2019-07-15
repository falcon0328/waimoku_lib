import unittest
from waimoku import *


class TestWaimokuUserListProvider(unittest.TestCase):
    def test_fetch_valid_file(self):
        """正常系　正しいデータのみが格納されているCSVファイルからユーザの一覧を取得するテスト
        """
        userListProvider = WaimokuUserListProvider()
        user_list = userListProvider.fetch(
            file_path="tests/res/event_132992_participants-3.csv")
        self.assertEqual(len(user_list), 78)
