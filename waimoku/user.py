from datetime import datetime
from .setsuei_status import WaimokuSetsueiStatus


class WaimokuUser:
    """ワイもくのユーザ情報
    """

    user_name: str
    display_name: str
    join_status: bool
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
                 join_status: bool,
                 participation_status: bool,
                 mokumoku: str,
                 is_handagote: bool,
                 is_survey: bool,
                 is_setsuei: WaimokuSetsueiStatus,
                 is_lt,
                 latest_update: datetime = datetime.now()):
        """イニシャライザ

        Arguments:
            user_name {str} -- ユーザ名
            display_name {str} -- 表示名
            join_status {bool} -- 参加ステータス
            participation_status {bool} -- 出席ステータス
            mokumoku {str} -- 本日のもくもく内容
            is_handagote {bool} -- はんだごてを利用するかどうか
            is_survey {bool} -- アンケートに同意したかどうか
            is_setsuei {WaimokuSetsueiStatus} -- 設営に協力するかどうか
            is_lt {bool} -- LTをするかどうか

        Keyword Arguments:
            latest_update {datetime.datetime} -- 最終更新日時 (default: {datetime.datetime.now()})
        """
        self.user_name = user_name
        self.display_name = display_name
        self.join_status = WaimokuUser.__join_status(
            join_status=join_status)
        self.participation_status = WaimokuUser.__participation_status(
            participation_status=participation_status)
        self.mokumoku = mokumoku
        self.is_handagote = WaimokuUser.__is_handagote(
            is_handagote=is_handagote)
        self.is_survey = WaimokuUser.__is_survey(is_survey=is_survey)
        self.is_setsuei = is_setsuei
        self.is_lt = is_lt
        self.latest_update = latest_update

    @classmethod
    def __join_status(cls, join_status: str) -> bool:
        return join_status == "参加"

    @classmethod
    def __participation_status(cls, participation_status: str) -> bool:
        return participation_status == "出席"

    @classmethod
    def __is_handagote(cls, is_handagote: str) -> bool:
        return is_handagote == "はい"

    @classmethod
    def __is_survey(cls, is_survey: str) -> bool:
        return is_survey == "理解しました"
