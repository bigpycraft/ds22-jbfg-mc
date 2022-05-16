"""
묵찌빠 게임

STEP1 : 게임시작 출력
STEP2 : 가위(0),바위(1),보(2)를 하여 공격/수비를 결정
STEP3 : [공격] or [수비] 묵(1), 찌(0), 빠(2) ?
STEP4 : 게임의 승부 or 공격/수비를 결정?
STEP5 : 결과메시지를 보여준다  

cf. 컴퓨터는 랜덤값, 플레이어는 입력값
"""
import random
import time

class GameMZP:
	# 속성
    player    = dict()     # 플레이어 {code:코드, disp:출력}
    computer  = dict()     # 컴퓨터

    is_draw   = bool()     # True:비김 (step=0, 가위바위보)
    is_over   = bool()     # True:종료 (step=1, 묵찌빠게임)

    is_attack = bool()     # True:공격, False:수비
    mode      = str()      # 공격/수비
    result    = str()      # 게임의결과 : Win/Lose
    play_cnt  = int()      # 게임카운트

    display = [
        { '0':'가위', '1':'바위', '2':'보' },
        { '0':'찌',   '1':'묵',  '2':'빠' },
    ]

    def __init__(self, player_name='사용자', computer_name='컴퓨터'):
        self.player_name = player_name
        self.computer_name = computer_name

    def start_game(self, step=0):
        """
            STEP1 : 게임시작 출력
        """
        print("묵찌빠 게임을 시작합니다!!!")
        self.is_draw = True
        self.is_over = False
        self.decide_attack_defense(step=0)


    def decide_attack_defense(self, step=0):
        """
            STEP2 : 가위바위보를 하여 공격과 수비모드를 결정한다.
        """
        time.sleep(1)
        print('-'*50)

        while self.is_draw:
            self.set_player(step=0)
            self.set_computer(step=0)
            self.decide_winner()
            time.sleep(1)

    def set_player(self, step=0):
        """
            사용자의 값을 입력 받는다.
                step=0 : 가위바위보 모드
                step=1 : 묵찌빠게임 모드
        """
        step = 0 if step==0 else 1
        if step == 0:
            guide_msg = "가위(0)/바위(1)/보(2) : "
            # code = input(guide_msg)

        else:
            self.mode = "공격" if self.is_attack else "수비"
            guide_msg = "[{}] 묵(1)/찌(0)/빠(2) : ".format(self.mode)
            # code = input(guide_msg)

        while True:
            code = input(guide_msg).strip()
            if code in list('012'):
                break
            else:
                print('잘못된 값입니다. 다시 입력해주세요!')

        self.player['code'] = code
        self.player['disp'] = self.display[step][code]

    def set_computer(self, step=0):
        step = 0 if step==0 else 1
        rnd_num = random.randint(0,2)
        code = str(rnd_num)

        self.computer['code'] = code
        self.computer['disp'] = self.display[step][code]

    def decide_winner(self):
        """
            가위바위보의 승부를 결정한다
        """
        if self.player['code'] == self.computer['code']:
            self.is_draw = True
            state = self.get_state()
            print(state, end=' => ')
            print('비겼습니다. 다시 한번더 시도하세요!')
        else:
            self.is_draw = False
            if ( (self.player['code'] == '0' and self.computer['code'] == '2') or
                 (self.player['code'] == '1' and self.computer['code'] == '0') or
                 (self.player['code'] == '2' and self.computer['code'] == '1') ):
                self.is_attack = True
            else:
                self.is_attack = False


    def play_game(self, step=1):
        """
            STEP3 : 묵찌빠 게임을 진행한다
        """
        time.sleep(1)
        print('-' * 50)

        cnt = 0
        # while not self.is_draw and not self.is_over:
        while not self.is_over:
            if cnt > 0:
                state = self.get_state()
                print(state)

            self.set_player(step)
            self.set_computer(step)

            self.decide_game_winner()
            cnt += 1
            time.sleep(1)

        self.play_cnt = cnt
        self.show_result_msg()


    def decide_game_winner(self):
        """
            STEP4 : 묵찌빠 게임의 승부를 결정한다
        """
        if self.player['code'] == self.computer['code']:
            self.is_over = True
            if self.mode == "공격":
                self.result = "You Win!!!"
            else:
                self.result = "You Lose!!!"

        else:
            self.is_over = False
            if ((self.player['code'] == '0' and self.computer['code'] == '2') or
                    (self.player['code'] == '1' and self.computer['code'] == '0') or
                    (self.player['code'] == '2' and self.computer['code'] == '1')):
                self.is_attack = True
                self.mode == "공격"
            else:
                self.is_attack = False
                self.mode == "수비"


    def show_result_msg(self):
        """
            STEP5 : 결과메시지를 보여준다
        """
        print('-' * 50)
        state = self.get_state()
        print(state)
        print('총 {}번의 시도를 하였습니다.'.format(self.play_cnt))
        print(self.result)


    def get_state(self):
        """
            사용자와 컴퓨터의 상태값을 확인한다.
        """
        state = '{p_name}:{p_disp}, {c_name}:{c_disp} '.format(
            p_name = self.player_name,
            p_disp = self.player['disp'],
            c_name = self.computer_name,
            c_disp = self.computer['disp']
        )
        # print(state)
        return state


if __name__ == "__main__":
    # gameMZP = GameMZP()
    # gameMZP = GameMZP('사용자', '컴퓨터')
    player_name   = '김진수'
    computer_name = '알파고'
    gameMZP = GameMZP(player_name, computer_name)

    gameMZP.start_game()
    print(gameMZP.get_state())

    gameMZP.play_game()
    print('-'*50)
    print("게임종료")
    print('-'*50)

