# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>Python Practice </font>
> 과제명 : 팩토리얼 표: 0~100 까지의 Factorial Table 
- 입력값에 대한 Validation Check
- Sum 값과 Factorial Table 출력


### Exemple Code

```python  

# 팩토리얼 표: 0~100 까지의 Factorial Table
idx, gop, sum  = 0, 0, 0
factorial = [ ]
total_sum = [ ]

# 입력값 확인
# num_check = list(range(10))
num_chk_list = list('0123456789')
# print(num_chk_list)

def is_num(str_num):
    '''
    입력값이 숫자값인지 아닌지를 확인하는 함수
    :param str_num: 입력값
    :return: True/False
    '''
    ret_num = True
    ret_msg = str()
    str_num = str(str_num)

    num_chk_list = list('0123456789')
    # num_chk_list = list(range(10))
    not_num_char = ''

    # print('check data : [{}]'.format(str_num))
    # print('num_chk_list : {}'.format(num_chk_list))
    for char in str_num:
        is_num = char in num_chk_list
        ret_num *= is_num
        # print('{} : {}'.format(char, is_num))
        if not is_num:
            not_num_char = char
            break

    if ret_num:
        last_num = int(key_in)
        ret_msg = '입력한 숫자 : {}'.format(last_num)
    else:
        ret_num = False
        ret_msg = '입력한 값이 숫자가 아닙니다. {}'.format(not_num_char)

    return ret_num, ret_msg


def cs_num(num):
    ret_num = str()

    str_num = str(num)
    # rev_num = list(str_num[::-1])
    rev_num = str_num[::-1]
    tmp_num = ''

    # print(type(rev_num), rev_num)

    for i in range(len(rev_num)):
        if i>0 and  i%3 == 0:
            tmp_num += ','
        tmp_num += rev_num[i]
        # print(i, tmp_num)

    ret_num = tmp_num[::-1]
    return ret_num



while True:
    key_in = input('숫자를 입력해 주세요.[1~100] => ')

    input_data = key_in.strip()
    ret_num, ret_msg = is_num(input_data)
    if ret_num:
        # print(ret_msg)
        break
    else:
        print(ret_msg)

# print('숫자확인 완료!')
# input_num = 10
input_num = int(input_data)

# 입력값이 숫자인 경우, 미션 수행
title = '# {} 팩토리얼 테이블'.format(input_num)
print('-'*50)
print(title)
print('-'*50)

numbers = list(range(input_num + 1))
# print('numbers :', numbers)

while idx < len(numbers):
    num = numbers[idx]
    sum += num
    gop *= num

    gop = 1 if gop<1 else gop
    # if gop < 1:
    #     gop = 1

    total_sum.append(sum)
    factorial.append(gop)
    idx += 1

# print(input_num, '까지의 합계는', total_sum[-1], '입니다.')
# print('아래는 팩토리얼 테이블입니다.')
for fact_num in range(len(factorial)):
    # print(str(fact_num)+'!\t= ', factorial[fact_num])
    # print(' {}! \t= {}'.format(fact_num, factorial[fact_num]))
    print(' {}! \t= {}'.format(fact_num, cs_num(factorial[fact_num])))


```


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
