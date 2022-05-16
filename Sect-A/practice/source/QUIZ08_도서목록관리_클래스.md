# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>Python Practice </font>
> 과제명 : 도서목록 관리 (Class기반의 OOP 프로그래밍) 
- 도서목록 입출력
- 조건에 맞는 데이터 조회



### Exemple Code

```python  
class BookManager:
    books = list()      # 책 목록 선언
    many_page = []
    recommends = []
    pub_companies = []
    all_pages = int()

    def reg_book(self):
        # 책 목록 만들기
        self.books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
        self.books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
        self.books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
        self.books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
        self.books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

    def get_many_page(self):
        self.many_page     = [ book['제목']  for book in self.books  if book['쪽수'] > 250 ]

    def get_recommends(self):
        self.recommends    = [ book['제목']  for book in self.books  if book['추천유무']  ]

    def get_pub_companies(self):
        pub_companies = { book['출판사'] for book in self.books }
        self.pub_companies = sorted(pub_companies)

    def get_all_pages(self):
        self.all_pages     = sum([book['쪽수'] for book in self.books])

    def final_display(self):
        print(' ### 도서 목록 출력 내용 ### \n', '-'*90)
        print(' 1. 쪽수가 250 쪽 넘는 책 리스트 :', self.many_page)
        print(' 2. 내가 추천하는 책 리스트      :', self.recommends)
        print(' 3. 내가 읽은 책 전체 쪽수       :', self.all_pages)
        print(' 4. 내가 읽은 책의 출판사 목록   :', sorted(self.pub_companies) )

bookManager = BookManager()
bookManager.reg_book()
bookManager.get_many_page()
bookManager.get_recommends()
bookManager.get_pub_companies()
bookManager.get_all_pages()

bookManager.final_display()

```


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
