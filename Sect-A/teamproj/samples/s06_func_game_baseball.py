# 야구게임
"""
    야구게임
    3자리 숫자값 맞히기
    S : 숫자와 자리수 같을 경우
    B : 숫자는 있고 자리수 다른경우
    몇번만에 맞히는지 최종 출력!!!
"""

# 1단계 : 3자리 랜던숫자 만들기
# 2단계 : 사용자입력값 판정
# 3단계 : 최종출력단

import random

def gen_numbers():
    str_num = str()

    while True:
        rnd_num = random.randint(100,999)
        str_num = str(rnd_num)
        if len(set(str_num)) == 3:
            break

    return str_num

def show_count(guess_num, hidden_num):
    is_correct = bool()
    f_msg = str()

    s_cnt = 0   # 스트라이크카운트
    b_cnt = 0   # 볼카운트

    if guess_num == hidden_num:
        is_correct = True
        f_msg = "삼진아웃"
    else:
        for idx in range(len(guess_num)):
            if guess_num[idx] == hidden_num[idx]:
                s_cnt += 1
            elif guess_num[idx] in list(hidden_num):
                b_cnt += 1
            else:
                pass

            # print("check : {}S {}B".format(s_cnt, b_cnt))

        is_correct = False
        f_msg = "{}Strike {}Ball".format(s_cnt, b_cnt)

    return is_correct, f_msg

# 1단계 : 3자리 랜던숫자 만들기
hidden_num = gen_numbers()
# print(hidden_num)
# print('숨겨진 숫자 : {} {} {}'.format(
#     hidden_num[0],
#     hidden_num[1],
#     hidden_num[2]
# ))
print("야구게임을 시작합니다^^")

# 2단계 : 사용자입력값 판정
try_count = 0
while True:
    try_count += 1
    guess_num = input("숫집입력 : ")
    guess_num = guess_num.strip()

    if len(guess_num) == 3:
        is_correct, f_msg = show_count(guess_num, hidden_num)
    else:
        print("3자리의 숫자를 입력해주세요.")
        continue

    # print("{}번 째 시도하였습니다.".format(try_count))
    if is_correct:
        print("[%d]"%try_count, f_msg)
        print("Correct Number : {}".format(hidden_num))
        print("게임종료!!!")
        break
    else:
        print("[%d]"%try_count, f_msg)

