import openpyxl as excel

from . import WaimokuUser


class WaimokuClient:
    __headerTitles: dict = {"A2": "通し番号", "B2": "区分", "C2": "氏名", "D2": "所属"}
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
            ws[key] = self.__headerTitles[key]
        for index, user in enumerate(user_list):
            ws["A{0}".format(index + 3)] = index + 1
            ws["C{0}".format(index + 3)] = user.full_name
            ws["D{0}".format(index + 3)] = user.assign
        # シートの幅を調節する
        self.__adjust_width(ws)
        # ファイル保存
        wb.save(save_filename)

    def __adjust_width(self, ws):
        """指定したシートの幅を調節する

        Arguments:
            ws {[]} -- 対象のシート
        """
        for index, col in enumerate(self.__cellWidths):
            ws.column_dimensions[excel.utils.get_column_letter(index + 1)].width = self.__cellWidths[index]
        return ws
