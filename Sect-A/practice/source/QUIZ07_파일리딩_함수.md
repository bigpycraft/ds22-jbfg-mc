# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>Python Practice </font>
> 과제명 : CSV파일 리딩 
- CSV(Comma Seperated Value) 파일을 읽어온다
- 도서목록관리에서 처럼 읽어온 데이터를 List(Dictionary) 형태로 저장



### Exemple Code

```python  

def read_csv(filename):
    # 파일데이터 읽어오기
    fp = open(filename, "r", encoding="utf-8")
    data = fp.read()
    fp.close()

    elements = []      # 최종 리턴하기 위한 리스트 변수

    rows = data.split("\n")     # 데이터를 한줄씩 구분하여 리스트로 담기

    for row in rows:
        fields = row.split(",")      # 한줄 데이터를 콤마(,)로 구분하여 리스트로 담기

        name   = fields[0].strip()   # 앞뒤의 빈공백을 없앤후 변수에 담기
        school = fields[1].strip()
        email  = fields[2].strip()
        element =  {
            "이름" : name ,
            "학교" : school,
            "메일" : email
        }

        elements.append(element)     # 한줄 데이터를 dict()형으로 변환후 리스트에 추가

    return elements


filename = "./data/students.csv"      # CSV파일명
students = read_csv(filename)         #

# print(students)

for student in students:
    print(student)

print('-'*50)
print(students[0]['이름'])

```


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
