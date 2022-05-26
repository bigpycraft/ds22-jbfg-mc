import openpyxl
from random import randint


def getUserScore(player_list):
    excel_file = '../Golf/data/golf_score_board.xlsx'
    wb = openpyxl.load_workbook(excel_file)
    ws = wb["스코어"]

    baseScore = []
    randomScore = []

    playerCnt = len(player_list)
    for c_num in range(3, 21):
        baseScore.append(ws.cell(column=c_num, row=2).value)

    for cnt in range(playerCnt):
        user = []
        for num in range(len(baseScore)):
            par = baseScore[num]
            user.append(randint(-2, par))
        randomScore.append(user)

    return randomScore, baseScore


def getStroke(player_list , randomScore):

    score = randomScore
    stroke = []

    for cnt in range(len(player_list)):
        stroke.append(72+sum(score[cnt]))

    return stroke


def getHandy(player_list):
    handy = []
    for cnt in range(len(player_list)):
        handy.append(0)

    return handy


def getTotalScore(randomScore, handyScore, player_list):
    score = []
    for i in range(len(player_list)):
        score.append(sum(randomScore[i]) - handyScore[i])

    return score


def getRank(score):
    total_list = score
    sort_list = sorted(total_list)
    rank_list = []

    for i in total_list:
        rank_list.append(sort_list.index(i) + 1)

    return rank_list


def getEbpbCnt(player_list, randomScore, baseScore):
    eagle_cnt = int()
    birdy_cnt = int()
    par_cnt = int()
    boggy_cnt = int()
    double_par_cnt = int()
    ebpbList = []

    for r in range(len(player_list)):
        for c in range(0,18):
            if (randomScore[r][c] == -2):
                eagle_cnt += 1
            elif (randomScore[r][c] == -1):
                birdy_cnt += 1
            elif (randomScore[r][c] == 0):
                par_cnt += 1
            elif (randomScore[r][c] == 1):
                boggy_cnt += 1
            elif (randomScore[r][c] == baseScore[c]):
                double_par_cnt += 1
            else:
                pass
        temp = [eagle_cnt, birdy_cnt, par_cnt, boggy_cnt, double_par_cnt]
        eagle_cnt, birdy_cnt, par_cnt, boggy_cnt, double_par_cnt = 0, 0, 0, 0, 0
        ebpbList.append(temp)

    return ebpbList