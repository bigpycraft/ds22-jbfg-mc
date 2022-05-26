import pck2_register as reg # 선수 및 랜덤스코어 등록
import pck3_calculator as cal # 점수 및 랭킹 계산
import pck4_count_records as cnt # 각종기록
import pck5_result_ranking as result1 # 대회결과 1
import pck6_result_records as result2 # 대회결과 2

# import pck_result_ranking as result # 각종기록

if __name__== "__main__":

    excel_file = './data/golf_score_board.xlsx'

    # 미션1 : 참가선수 등록
    is_success, result_msg = reg.reg_player(excel_file)
    if is_success: print(result_msg)

    # 미션2 : 참가선수들 HOLE별 스코어를 랜덤하게 입력 (-2 ~ PAR)
    is_success, result_msg = reg.reg_score_mgr(excel_file)
    if is_success: print(result_msg)

    # 미션3 : 18홀까지의 스코어, 보정치를 계산하여 등록 (핸디는 옵션)

    ## (1) 스트로크 계산하기
    is_success, result_msg = cal.cal_stroke(excel_file)
    if is_success: print(result_msg)

    ## (2) 핸디 보정치 Default=0
    is_success, result_msg = cal.cal_handy(excel_file)
    if is_success: print(result_msg)

    ## (3) 최종성적
    is_success, result_msg = cal.cal_final_score(excel_file)
    if is_success: print(result_msg)

    # 미션4: 보정치 기준으로 랭킹 등록, 각종 기록 갯수 등록

    ## (1) 순위 매기기 ranking
    is_success, result_msg = cnt.cal_ranking(excel_file)
    if is_success: print(result_msg)

    ## (2) 각종기록 cnt_records
    is_success, result_msg = cnt.cnt_records(excel_file)
    if is_success: print(result_msg)

    # 미션5: 대회결과 시트에 결과에 맞는 선수명과 최종성적/기록수를 등록

    ## (1) 대회결과 result(랭킹)
    is_success, result_msg = result1.result_ranking(excel_file)
    if is_success: print(result_msg)

    ## (2) 대회결과 result(기록)
    is_success, result_msg = result2.result_records(excel_file)
    if is_success: print(result_msg)
