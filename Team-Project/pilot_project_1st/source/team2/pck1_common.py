import openpyxl
import random
from openpyxl.utils import get_column_letter #컬럼값을 숫자값으로 변경

# Common : 엑셀 로딩
def excel_loading(excel_file, sheet_name=None):
    wb = openpyxl.load_workbook(excel_file)
    if bool(sheet_name):
        ws = wb[sheet_name]
    else:
        ws = wb.active
    return wb, ws


# For Module Test!!!!
if __name__ == "__main__":
    # excel_file = './data/golf_score_board_test.xlsx'
    # is_success = reg_score_mgr(excel_file)
    # print(is_success)
    print('random_scoring_main....')
