# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>실습 프로젝트, Practice Project</font>
> 실습 프로젝트1
- 구구단 출력하기
- 총합과 팩토리얼 테이블 출력하기
- 문자열 바꾸기 
- 대소문자 변경
- 도서 목록 입력 및 출력

> 실습 프로젝트2 
- 그래픽(Turtle Graphics) 출력하기
- 모양 그리기, 다각형 그리기
- 패턴을 찾아 모양을 그리기


## 구구단 출력

### <font color='blue'> 원하는 구구단 출력 </font>


```python
dan = input('출력할 단을 입력해주세요.[2~9] ')
# dan = 5
dan = int(dan)
gop = 0

print(dan, '단 출 력 \n' + '-'*20)
# print(dan, '단 출 력 - Case1\n' + '-'*20)
for i in range(9):
    num = i + 1
    gop = dan * num
    print(dan, '*', num, '=', gop)

```

    출력할 단을 입력해주세요.[2~9] 5
    5 단 출 력 
    --------------------
    5 * 1 = 5
    5 * 2 = 10
    5 * 3 = 15
    5 * 4 = 20
    5 * 5 = 25
    5 * 6 = 30
    5 * 7 = 35
    5 * 8 = 40
    5 * 9 = 45
    

### <font color='blue'> 구구단 전체 출력 </font>

``` python
for m in range(2, 10):
    print('%s \n [%d 단 출 력]' % ('='*16, m))
    for n in range(1, 10):
        print('  {} x {} = {}'.format(m, n, m*n))
```


```python
# 구구단 전체 출력
cols = 4
rows = int(8/cols)+1
w_space = '\t\t'

for row in range(rows):

    dans = list()
    for col in range(cols):
        dan = (row * cols) + col + 2
        dans.append(dan)

    for num in range(10):
        for dan in dans:
            if dan > 9:
                continue

            if num<1:
                print('{} 단 \t'.format(dan), end=w_space)
            else:
                gugutext = '{} x {} = {}'.format(dan, num, dan*num)
                print(gugutext, end=w_space)
        print()

    print()


```

    2 단 			3 단 			4 단 			5 단 			
    2 x 1 = 2		3 x 1 = 3		4 x 1 = 4		5 x 1 = 5		
    2 x 2 = 4		3 x 2 = 6		4 x 2 = 8		5 x 2 = 10		
    2 x 3 = 6		3 x 3 = 9		4 x 3 = 12		5 x 3 = 15		
    2 x 4 = 8		3 x 4 = 12		4 x 4 = 16		5 x 4 = 20		
    2 x 5 = 10		3 x 5 = 15		4 x 5 = 20		5 x 5 = 25		
    2 x 6 = 12		3 x 6 = 18		4 x 6 = 24		5 x 6 = 30		
    2 x 7 = 14		3 x 7 = 21		4 x 7 = 28		5 x 7 = 35		
    2 x 8 = 16		3 x 8 = 24		4 x 8 = 32		5 x 8 = 40		
    2 x 9 = 18		3 x 9 = 27		4 x 9 = 36		5 x 9 = 45		
    
    6 단 			7 단 			8 단 			9 단 			
    6 x 1 = 6		7 x 1 = 7		8 x 1 = 8		9 x 1 = 9		
    6 x 2 = 12		7 x 2 = 14		8 x 2 = 16		9 x 2 = 18		
    6 x 3 = 18		7 x 3 = 21		8 x 3 = 24		9 x 3 = 27		
    6 x 4 = 24		7 x 4 = 28		8 x 4 = 32		9 x 4 = 36		
    6 x 5 = 30		7 x 5 = 35		8 x 5 = 40		9 x 5 = 45		
    6 x 6 = 36		7 x 6 = 42		8 x 6 = 48		9 x 6 = 54		
    6 x 7 = 42		7 x 7 = 49		8 x 7 = 56		9 x 7 = 63		
    6 x 8 = 48		7 x 8 = 56		8 x 8 = 64		9 x 8 = 72		
    6 x 9 = 54		7 x 9 = 63		8 x 9 = 72		9 x 9 = 81		
    
    
    
    
    
    
    
    
    
    
    
    
    

### 문자열 대소문자 바꾸기


```python
# swap case
# s = 'The BigpyCraft find the information to design valuable society with Technology & Craft.'
s = input('영어 대소문자로 이루어진 문장을 입력하세요.\n')  # 문자열 입력

print('모두 대문자로 출력\n' + s.upper())   # 대문자로 모두 변환

print('모두 소문자로 출력\n' + s.lower())   # 소문자로 모두 변환

new_s = str()   # 신규 문자열 형 변수 선언

for c in s:     # 입력 받은 문자를 하나씩 꺼내서 c에 대입

    if c.islower():         # 해당 문자가 소문자이면
        new_s += c.upper()  # 대문자로 변경하여 new_s에 붙이기
    else:                   # 해당 문자가 대문자이면
        new_s += c.lower()  # 소문자로 변경하여 new_s에 붙이

print('대소문자 바꿔서 출력\n' + new_s)             # 최종 변환 결과 출력

print('대소문자 바꿔서 출력\n' + s.swapcase())      # 대소문자 모두 변환


```

    영어 대소문자로 이루어진 문장을 입력하세요.
    The BigpyCraft find the information to design valuable society with Technology & Craft.
    모두 대문자로 출력
    THE BIGPYCRAFT FIND THE INFORMATION TO DESIGN VALUABLE SOCIETY WITH TECHNOLOGY & CRAFT.
    모두 소문자로 출력
    the bigpycraft find the information to design valuable society with technology & craft.
    대소문자 바꿔서 출력
    tHE bIGPYcRAFT FIND THE INFORMATION TO DESIGN VALUABLE SOCIETY WITH tECHNOLOGY & cRAFT.
    대소문자 바꿔서 출력
    tHE bIGPYcRAFT FIND THE INFORMATION TO DESIGN VALUABLE SOCIETY WITH tECHNOLOGY & cRAFT.
    

### 문자열 순서 바꾸기


```python
# reverse case
# s = 'Life is too short, You nee Python.'
s = input('영어 문장을 입력하세요.\n')  # 문자열 입력

new_s = str()                       # 신규 문자열형 변수 선언

for x in range(len(s)-1, -1, -1):   # range()를 활용한 역순 인덱스 추출
    new_s += s[x]                   # 문자열을 끝에서부터 앞으로 신규 변수에 붙이기

print(new_s)                        # 위 결과 출력

print(s[::-1])                      # 인덱스 사용법으로 역순 출력

```

    영어 문장을 입력하세요.
    Life is too short, You nee Python.
    .nohtyP een uoY ,trohs oot si efiL
    .nohtyP een uoY ,trohs oot si efiL
    

### 도서 목록 입력 및 출력


```python
books = list()      # 책 목록 선언

# 책 목록 만들기
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

for book in books:  # 책 한 권씩 꺼내기 위한 루프 선언
    print(book)     # 책 한 권 데이터 출력

```

    {'제목': '파이썬 프로그램', '출판연도': '2016', '출판사': 'A', '쪽수': 200, '추천유무': False}
    {'제목': '플랫폼 비즈니스', '출판연도': '2013', '출판사': 'B', '쪽수': 584, '추천유무': True}
    {'제목': '빅데이터 마케팅', '출판연도': '2014', '출판사': 'A', '쪽수': 296, '추천유무': True}
    {'제목': '외식경영 전문가', '출판연도': '2010', '출판사': 'B', '쪽수': 526, '추천유무': False}
    {'제목': '십억만 벌어보자', '출판연도': '2013', '출판사': 'A', '쪽수': 248, '추천유무': True}
    


```python
# case 1
many_page = list()                              # 책 리스트 선언
recommends = list()                             # 책 리스트 선언
all_pages = int()                               # 전체 쪽수 변수 선언
pub_companies = set()                           # 출판사 집합 선

for book in books:                              # 책 한 권씩 꺼내기 위한 루프 선언
    if book['쪽수'] > 250:                       # 250쪽 넘는 책 목록 만들기
        many_page.append(book['제목'])
    if book['추천유무']:                          # 책 추천 목록 만들기
        recommends.append(book['제목'])
    all_pages = all_pages + book['쪽수']         # 책 쪽수 더하기
    pub_companies.add(book['출판사'])

print('쪽수가 250 쪽 넘는 책 리스트:', many_page)
print('내가 추천하는 책 리스트:', recommends)
print('내가 읽은 책 전체 쪽수:', all_pages)
print('내가 읽은 책의 출판사 목록:', pub_companies)

```

    쪽수가 250 쪽 넘는 책 리스트: ['플랫폼 비즈니스', '빅데이터 마케팅', '외식경영 전문가']
    내가 추천하는 책 리스트: ['플랫폼 비즈니스', '빅데이터 마케팅', '십억만 벌어보자']
    내가 읽은 책 전체 쪽수: 1854
    내가 읽은 책의 출판사 목록: {'B', 'A'}
    


```python
total_sum = sum([1, 2, 3, 4, 5])
total_sum
```




    15




```python
# case 2
many_page     = [ book['제목']  for book in books  if book['쪽수'] > 250 ]
recommends    = [ book['제목']  for book in books  if book['추천유무']  ]
pub_companies = { book['출판사'] for book in books }
all_pages     = sum([book['쪽수'] for book in books])

print(' ### 도서 목록 출력 내용 ### \n', '-'*90)
print(' 1. 쪽수가 250 쪽 넘는 책 리스트 :', many_page)
print(' 2. 내가 추천하는 책 리스트      :', recommends)
print(' 3. 내가 읽은 책 전체 쪽수       :', all_pages)
print(' 4. 내가 읽은 책의 출판사 목록   :', sorted(pub_companies) )
```

     ### 도서 목록 출력 내용 ### 
     ------------------------------------------------------------------------------------------
     1. 쪽수가 250 쪽 넘는 책 리스트 : ['플랫폼 비즈니스', '빅데이터 마케팅', '외식경영 전문가']
     2. 내가 추천하는 책 리스트      : ['플랫폼 비즈니스', '빅데이터 마케팅', '십억만 벌어보자']
     3. 내가 읽은 책 전체 쪽수       : 1854
     4. 내가 읽은 책의 출판사 목록   : ['A', 'B']
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
