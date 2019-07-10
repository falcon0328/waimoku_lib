from enum import Enum


class WaimokuJoinStatus(Enum):
    """ワイもくの参加ステータス（connpass準拠）

    Arguments:
        Enum {int} -- 0: 参加, 1: キャンセル
    """
    join = 0
    canceld = 1
