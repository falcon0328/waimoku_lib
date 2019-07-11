from datetime import datetime
from .participationn_status import WaimokuJoinStatus
from .setsuei_status import WaimokuSetsueiStatus


class WaimokuUser:
    """ワイもくのユーザ情報
    """

    user_name: str
    display_name: str
    join_status: WaimokuJoinStatus
    participation_status: bool
    mokumoku: str
    is_handagote: bool
    is_enquete: bool
    is_setsuei: WaimokuSetsueiStatus
    is_lt: bool
    latest_update: datetime

    def __init__(self,
                 user_name: str,
                 display_name: str,
                 join_status: WaimokuJoinStatus,
                 participation_status: bool,
                 mokumoku: str,
                 is_handagote: bool,
                 is_enquete: bool,
                 is_setsuei: WaimokuSetsueiStatus,
                 is_lt,
                 latest_update: datetime = datetime.now()):
        """イニシャライザ

        Arguments:
            user_name {str} -- ユーザ名
            display_name {str} -- 表示名
            join_status {WaimokuJoinStatus} -- 参加ステータス
            participation_status {bool} -- 出席ステータス
            mokumoku {str} -- 本日のもくもく内容
            is_handagote {bool} -- はんだごてを利用するかどうか
            is_enquete {bool} -- アンケートに同意したかどうか
            is_setsuei {WaimokuSetsueiStatus} -- 設営に協力するかどうか
            is_lt {bool} -- LTをするかどうか

        Keyword Arguments:
            latest_update {datetime.datetime} -- 最終更新日時 (default: {datetime.datetime.now()})
        """
        self.user_name = user_name
        self.display_name = display_name
        self.join_status = join_status
        self.participation_status = participation_status
        self.mokumoku = mokumoku
        self.is_handagote = is_handagote
        self.is_enquete = is_enquete
        self.is_setsuei = is_setsuei
        self.is_lt = is_lt
        self.latest_update = latest_update
