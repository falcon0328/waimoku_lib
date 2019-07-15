import pandas as pd
from .user import WaimokuUser
from .setsuei_status import WaimokuSetsueiStatus


class WaimokuUserListProvider:
    raw_data: pd.DataFrame

    def fetch(self, file_path: str, encoding: str = "cp932") -> list:
        user_list = []
        """指定されたファイルパスに存在するファイルからユーザ一覧を取得する

        Arguments:
            file_path {str} -- ファイルパス
        """
        self.raw_data = pd.read_csv(file_path, encoding=encoding)
        for data in self.raw_data.itertuples():
            user = WaimokuUser(user_name=data[2],
                               display_name=data[3],
                               full_name=data[7],
                               assign=data[8],
                               join_status=None,
                               participation_status=None,
                               mokumoku=data[9],
                               is_handagote=True,
                               is_survey=True,
                               is_setsuei=None,
                               is_lt=False,
                               latest_update=data[15])
            user_list.append(user)
        return user_list
