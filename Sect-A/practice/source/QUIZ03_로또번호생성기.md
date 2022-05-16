# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>Python Practice </font>
> 과제명 : 로또번호 생성기   
<br/> ▣ 로또번호 티켓 개수를 입력받은 후, 순차적으로 정렬하여 출력해보자
<br/> ▣ Hint : 로또번호는 1에서 45까지의 번호중 랜덤하게 6개 숫자 발급


```python  
from random import randint 
pick_number = randint(1, 45)    # 1에서 45까지의 랜덤정수를 생성
```
<!--
<실행결과>  python.exe 과제3.py

##### 로또번호 생성기 #####
발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => 0
한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요
발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => 7
한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요
발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => 5
5개의 로또번호 티켓을 주문하셨습니다.
------------------------------------------------------------------------------------------
 * 티켓1 : [1, 5, 9, 18, 28, 34]
 * 티켓2 : [1, 5, 22, 25, 42, 44]
 * 티켓3 : [3, 14, 22, 33, 39, 44]
 * 티켓4 : [1, 9, 11, 23, 24, 29]
 * 티켓5 : [10, 11, 14, 23, 34, 42]
------------------------------------------------------------------------------------------
생성한 로또번호는 최종적으로 dict형으로 저장 
final_ticket = {'티켓1': [1, 5, 9, 18, 28, 34], '티켓2': [1, 5, 22, 25, 42, 44], '티켓3': [3, 14, 22, 33, 39, 44], '티켓4': [1, 9, 11, 23, 24, 29], '티켓5': [10, 11, 14, 23, 34, 42]}
-->
### Exemple Code


```python
"""
    과제 : 로또번호생성기
    Detail : 생성할 로또번호(45개의 번호중 6개번호) 티켓 갯수 입력받은후, 슬립용지에 로또번호리스트를 순차적으로 정렬하여 출력한다.
    Input  : 티켓 갯수 [1~5]
    Oupput : 로또번호 슬립용지 출력

"""
from random import randint

LOTTO_NUM_CNT = 6

print('##### 로또번호 생성기 #####')

while True:
    t_count = input('발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => ')
    t_count = int(t_count.strip())

    if t_count<=0 or t_count > 5:
        print('한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요')
    else:
        print('%d개의 로또번호 티켓을 주문하셨습니다.'%t_count)
        break

print('-'*90)

final_ticket = dict()
t_no = 0

while t_no < t_count:

    lotto_number = set()
    while True:
        pick_number = randint(1, 45)     # 1에서 45까지의 랜덤정수를 생성

        lotto_number.add(pick_number)
        if len(lotto_number) == LOTTO_NUM_CNT:
            break
        else:
            continue

    t_val = sorted(lotto_number)

    t_no += 1
    t_key = '티켓%d'%t_no
    print(' * {} : {}'.format(t_key, t_val))

    final_ticket[t_key] = t_val

print('-'*90)
print('생성한 로또번호는 최종적으로 dict형으로 저장 \nfinal_ticket = {}'.format(final_ticket))
```

    ##### 로또번호 생성기 #####
    발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => 0
    한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요
    발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => 7
    한번에 발급할 수 있는 티켓은 최소 1개에서 최대 5개입니다. 다시입력해주세요
    발급할 로또번호 티켓 갯수를 입력하세요.[1~5] => 5
    5개의 로또번호 티켓을 주문하셨습니다.
    ------------------------------------------------------------------------------------------
     * 티켓1 : [1, 5, 9, 18, 28, 34]
     * 티켓2 : [1, 5, 22, 25, 42, 44]
     * 티켓3 : [3, 14, 22, 33, 39, 44]
     * 티켓4 : [1, 9, 11, 23, 24, 29]
     * 티켓5 : [10, 11, 14, 23, 34, 42]
    ------------------------------------------------------------------------------------------
    생성한 로또번호는 최종적으로 dict형으로 저장 
    final_ticket = {'티켓1': [1, 5, 9, 18, 28, 34], '티켓2': [1, 5, 22, 25, 42, 44], '티켓3': [3, 14, 22, 33, 39, 44], '티켓4': [1, 9, 11, 23, 24, 29], '티켓5': [10, 11, 14, 23, 34, 42]}
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
