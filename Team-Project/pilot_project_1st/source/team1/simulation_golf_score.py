# from Packages import golf_socre_mgr_v8 as gsm
from proj1st.team1.Packages import golf_socre_mgr_v8 as gsm


if __name__ == "__main__":
    print('테스트 시작!!!')

    player_file = "data/명단.txt"
    excel_file  = "data/golf_score_board.xlsx"

    # 미션1 : 참가선수들 등록 (실시간입력/등록명단파일호출)
    player = gsm.선수등록(excel_file, player_file)

    # 미션2 : 참가선수들 HOLE별 스코어를 랜덤하게 입력
    gsm.난수뿌리기(excel_file, player)

    # 미션3 : 18홀까지의 스코어, 보정치를 계산하여 등록 (핸디는 옵션), 보정치는 없다.
    gsm.스트로크합산(excel_file, player)

    # 미션4 : 보정치 기준으로 랭킹 등록, 각종 기록 갯수 등록
    gsm.기록등록(excel_file, player)

    # 미션5 : 대회결과 시트에 결과에 맞는 선수명과 최종성적/기록수를 등록
    msg = gsm.대회결과등록(excel_file, player)
    print(msg)

    print('테스트 종료!!!')