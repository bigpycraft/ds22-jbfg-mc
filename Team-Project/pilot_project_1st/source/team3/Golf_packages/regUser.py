import openpyxl
from proj1st.team3.Golf_packages import readCSV


def regUsers():
    excel_file = './data/golf_score_board.xlsx'
    wb = openpyxl.load_workbook(excel_file)
    ws = wb['스코어']
    filename = "./data/참석자명단.csv"  # CSV파일명

    user_list = readCSV.read_csv(filename)

    # 신규 유저 리스트 등록
    print('사용자 등록을 시작합니다.')
    for r in range(len(user_list)):
        ws.cell(row=r+3, column=1, value=user_list[r])

    wb.save(excel_file)
    print('총 {}명의 사용자가 등록 되었습니다.'.format(len(user_list)))

    return user_list
