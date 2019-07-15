import openpyxl as excel
from openpyxl.styles.fonts import Font
from openpyxl.utils import get_column_letter
from openpyxl.styles.alignment import Alignment
from . import WaimokuUser


class WaimokuClient:
    __headerTitles: dict = {"A2": "通し番号", "B2": "区分", "C2": "氏名", "D2": "所属"}
    __font_sizes: list = [9, 9, 11, 11]
    __cellWidths: list = [6.83, 4.83, 17.33, 44.67]

    def save_to_file(self, user_list: [WaimokuUser], save_filename="event_participantsList.xlsx"):
        # ブックの新規作成
        wb = excel.Workbook()
        # アクティブなシートの作成
        ws = wb.active
        # シートタイトルはSheet1に変更
        ws.title = "Sheet1"
        # ヘッダーを用意
        for key in self.__headerTitles.keys():
            self.write(ws=ws, key=key, value=self.__headerTitles[key], font_size=9)
        # シートにデータを書き込む
        for index, user in enumerate(user_list):
            self.write(ws=ws, key="A{0}".format(index + 3), value=index+1, font_size=9)
            self.write(ws=ws, key="C{0}".format(index + 3), value=user.full_name, font_size=11)
            self.write(ws=ws, key="D{0}".format(index + 3), value=user.assign, font_size=11)
        # シートの幅を調節する
        self.__adjust_sheet_size(ws)
        # 全てのセルに上下中央揃えを実施
        self.__adjust_sheet_alignment(ws)
        # ファイル保存
        wb.save(save_filename)

    def write(self, ws, key: str, value, font_size: int = 9):
        """ワークシートの指定したキーにデータを書き込む

        Arguments:
            ws {} -- 対象のワークシート
            key {str} -- キー
            value {} -- 書き込む内容

        Keyword Arguments:
            font_size {int} -- フォントサイズ (default: {9})
        """
        ws[key] = value
        ws[key].font = Font(size=font_size)

    def __adjust_sheet_size(self, ws):
        """指定したシートの幅を調節する

        Arguments:
            ws {[]} -- 対象のシート
        """
        for index, col in enumerate(self.__cellWidths):
            ws.column_dimensions[excel.utils.get_column_letter(index + 1)].width = self.__cellWidths[index]
        for row in range(ws.max_row + 1):
            ws.row_dimensions[row].height = 27

    def __adjust_sheet_alignment(self, ws, align: Alignment = Alignment(vertical="center")):
        """セルの値を上下左右、指定した価値に揃える

        Arguments:
            ws {[type]} -- 対象のシート

        Keyword Arguments:
            align {Alignment} -- アライン情報 (default: {Alignment(vertical="center")})
        """
        for row in ws:
            for cell in row:
                cell.alignment = align
