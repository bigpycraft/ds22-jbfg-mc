# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>Python Practice </font>
> 과제명 : 환율계산기   
<br/> ▣ 현재의 환율정보를 입력 받아서 리스트로 출력해 보자.
<br/>  - 송금시의 보낼 때, 받을 때 정보를 입력받아, 숫자형 리스트로 출력
<br/> ▣ 미화로 보낼 때와 한화로 보낼 때, 받게 될 금액을 계산해보자
<br/>  - 송금 환율 리스트를 기준으로 입력한 송금액 계산해서 출력


※ 참조. 환율/외화예금 금리
<br/>  https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp
<!--
<실행결과>  python.exe 과제2.py

##### 환율계산기(KRW/USD) #####
보낼 떄 송금 환율을 입력하세요 => 1,123.40
받을 떄 송금 환율을 입력하세요 => 1,102.60
---------------------------------------------------------------------------------------
[NOTICE]
 * 현재의 송금 환율은 보낼 때 1,123.40, 받을 떄 1,102.60입니다.
 * 송금환율 리스트 [보낼때, 받을때] :  [1123.4, 1102.6]
---------------------------------------------------------------------------------------
미국에서 송금할 미화(USD) 금액을 입력하세요 => 1000
한국에서 송금할 한화(KRW) 금액을 입력하세요 => 1124400
---------------------------------------------------------------------------------------
[RESULT]
 * 받을 떄 : 1000.00 USD => 1102600 KRW
 * 보낼 떄 : 1124400 KRW => 1000.00 USD
-->
### Exemple Code


```python
"""
    과제 : 환율계산기
    Detail : 원화, 환율을 입력받아 달러와흘 출력하는 환율 계산기
    Input  : 원화, 환율
    Oupput : 달러화

"""
print("##### 환율계산기(KRW/USD) #####")
rate_s = input('보낼 떄 송금 환율을 입력하세요 => ')
rate_r = input('받을 떄 송금 환율을 입력하세요 => ')
# rate_s, rate_r = '1,124.40', '1,102.60'

print('-'*80)
print('[NOTICE]')
print(' * 현재의 송금 환율은 보낼 때 {}, 받을 떄 {}입니다. '.format(rate_s, rate_r))

rate_s = rate_s.replace(' ', '')
rate_s = rate_s.replace(',', '')
rate_s = float(rate_s)

rate_r = rate_r.replace(' ', '')
rate_r = rate_r.replace(',', '')
rate_r = float(rate_r)

rate_list = []
rate_list.append(rate_s)
rate_list.append(rate_r)
print(" * 송금환율 리스트 [보낼때, 받을때] : ", rate_list)
print('-'*80)
m1_usd_send = input('미국에서 송금할 미화(USD) 금액을 입력하세요 => ')
m2_krw_send = input('한국에서 송금할 한화(KRW) 금액을 입력하세요 => ')
m1_usd_send = float(m1_usd_send)
m2_krw_send = int(m2_krw_send)
# m1_usd_send = 1000
m1_krw_recv = m1_usd_send * rate_list[1]
print('-'*80)
print('[RESULT]')
msg = ' * 받을 떄 : %.2f USD => %d KRW' % (m1_usd_send, m1_krw_recv)
print(msg)

# m2_krw_send = 1124400
m2_usd_recv = m2_krw_send / rate_list[0]
msg = ' * 보낼 떄 : %d KRW => %.2f USD' % (m2_krw_send, m2_usd_recv)
print(msg)


```

    ##### 환율계산기(KRW/USD) #####
    보낼 떄 송금 환율을 입력하세요 => 1,124.40
    받을 떄 송금 환율을 입력하세요 => 1,102.60
    --------------------------------------------------------------------------------
    [NOTICE]
     * 현재의 송금 환율은 보낼 때 1,124.40, 받을 떄 1,102.60입니다. 
     * 송금환율 리스트 [보낼때, 받을때] :  [1124.4, 1102.6]
    --------------------------------------------------------------------------------
    미국에서 송금할 미화(USD) 금액을 입력하세요 => 1000
    한국에서 송금할 한화(KRW) 금액을 입력하세요 => 1124400
    --------------------------------------------------------------------------------
    [RESULT]
     * 받을 떄 : 1000.00 USD => 1102600 KRW
     * 보낼 떄 : 1124400 KRW => 1000.00 USD
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
