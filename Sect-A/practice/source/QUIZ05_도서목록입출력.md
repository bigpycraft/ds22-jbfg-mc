# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>Python Practice </font>
> 과제명 : 도서목록 관리  
- 도서목록 입출력
- 조건에 맞는 데이터 조회



### Exemple Code1

```python  
books = list()      # 책 목록 선언

# 책 목록 만들기
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

for book in books:  # 책 한 권씩 꺼내기 위한 루프 선언
    print(book['제목'], book['출판연도'])     # 책 한 권 데이터 출력

```



### Exemple Code2

```python 
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


### Exemple Code3

```python 
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



<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
