
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>정규식, Regular Expression</font>
>  
- 정규 표현식
- 문자열에서 특정 문자 조합을 찾기 위한 패턴



### RegEx 예제


```python

import re

# 테스트용 문자열 저장
text = 'My id number is [G203_5A]'
print("# 테스트 문자열 : %s \n%s" % (text, '-'*50))

# 소문자 a 찾기
result = re.findall('a', text)
print(result)

# 대문자 A 찾기
result = re.findall('A', text)
print(result)

# 소문자 i 찾기
result = re.findall('i', text)
print(result)

# 소문자 찾기
result = re.findall('[a-z]', text)
print(result)

# 소문자 연속해서 찾기
result = re.findall('[a-z]+', text)
print(result)

# 대문자 찾기
result = re.findall('[A-Z]', text)
print(result)

# 숫자 찾기
result = re.findall('[0-9]', text)
print(result)

# 숫자 연속해서 찾기
result = re.findall('[0-9]+', text)
print(result)

# 영문자 및 숫자 찾기
result = re.findall('[a-zA-Z0-9]', text)
print(result)

# 영문자 및 숫자 연속해서 찾기
result = re.findall('[a-zA-Z0-9]+', text)
print(result)

# 영문자/숫자 아닌 문자 찾기
result = re.findall('[^a-zA-Z0-9]', text)
print(result)

# 영문자 및 '_'특수기호 찾기
result = re.findall('[\w]', text)
print(result)

# 영문자 및 '_'특수기호 연속해서 찾기
result = re.findall('[\w]+', text)
print(result)

# 영문자 및 '_'특수기호 아닌 문자 찾기
result = re.findall('[\W]', text)
print(result)

```


### RegEx 예제2


```python

import re

text = """
옛날 옛적에 김진수라는 사람이 살았습니다.
그에게는 5형제가 있었는데, 김진수, 김진구, 김진용, 김진태, 김진욱 이렇게 다섯명 있었습니다.
그리고 그는 결혼을 해서 김찬영, 김준영, 김채영 3남매를 낳고 알콩달콩 행복하게 잘 살았습니다.
채영이가 좋아하는 사촌은 김예영이랑 김민영이랍니다. 김서영이는 본지가 너무 오래되었네요.
"""
# 형제 : 김진O
# 자녀 : 김O영

print('-'*70, '\n# 형제들 이름 찾기')
pattern = re.compile("김진\w")

brother = pattern.findall(text)
# print(brother)

brother = sorted(set(brother))
print(brother)

print('-'*70, '\n# 아이들 이름 찾기')
pattern = re.compile("김\w영")

children = pattern.findall(text)
print(children)

```


### RegEx 예제3

```python

import re

# 010-5670-3847
# 010-오륙칠공-3847
# 공일빵 5670 3팔4칠
# cf. 0.5% 정도는 저런사람 있쥐요~
text = """
    010-5670-3847   # space, -, . => []
    010 5670 3847
    010.5670 3847
"""
print('-'*70, '\n# 핸드폰 번호 찾기')
pattern = re.compile("\d{3}[ -.]?\d{4}[ -.]?\d{4}")
phone_no = pattern.findall(text)
print(phone_no)

```

### RegEx 예제4

```python

import re

text = """
    010-5670-3847   # space, -, . => []
    옛날에는 011-1052-3847 이랬는데..
    010 5670 3847
    010.-5670 3847
    010-오륙칠공-3847
    공일빵 5670 3팔4칠
    사는동네가 자이아파트 516동512호
    그리구, 사무실번호는 02-360-4047이고
    우편번호는 100-791, 청파로 463번지
"""

print('-'*70, '\n# 핸드폰 번호 찾기')
pattern = re.compile("\d{3}[ -.]?\d{4}[ -.]?\d{4}")
phone_no = pattern.findall(text)
print(phone_no)

print('-'*70, '\n# 핸드폰 번호 찾기2')
pattern = re.compile("\d{2,3}[ -\.]?\d{3,4}[ -\.]?\d{4}")
phone_no = pattern.findall(text)
print(phone_no)

print('-'*70, '\n# 핸드폰 번호 찾기3')
pattern = re.compile("\d{3}[ -\.]{1,2}\d{3,4}[ -\.]?\d{4}")
phone_no = pattern.findall(text)
print(phone_no)

```




### Regular Expression 관련 사이트
- Text 정보를 re로 테스트 : https://regexr.com/
- re를 다이어그램으로 표현 : https://regexper.com/


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
