
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>JSON 핸들링</font>
>  JSON (JavaScript Object Notation)은 경량의 DATA-교환 형식
- JSON 인코딩/디코딩
- List 형태의 JSON 로딩
- Dict 형태의 JSON 로딩


### 파일 I/O


### JSON 인코딩/디코딩
```python
import json

json_data = {
    'firstname' : '길동',
    'lastname'  : '홍',
    'age'       : 20,
    'country'   : '율도국'
}

# json_code = json.JSONEncoder().encode(json_data)
json_code = json.JSONEncoder(ensure_ascii=False).encode(json_data)
print(json_code)
print(type(json_code))
# print(json_code['country'])

json_code = json.JSONDecoder().decode(json_code)
print(json_code)
print(type(json_code))
print(json_code['country'])

print('-'*50)
text = "{}{}은 {}살 이고, {}에 살고 있습니다.".format(
    json_code['lastname'],
    json_code['firstname'],
    json_code['age'],
    json_code['country'],
)

print(text)
```

### 파이썬 객체
```python
class Person:
    name = str()
    age = int()
    hometown = str()

    def __init__(self, name, age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

    def to_string(self):
        # str = '나의 살던 고향은 ' + self.hometown + '입니다.'
        str = '%s의 나이는 %d살이고, 고향은 %s입니다.' % (self.name, self.age, self.hometown)
        return str

theif1 = Person("홍길동", 20, "율도국");
theif2 = Person("임꺽정", 35, "구월산");

print(theif1.to_string())
print(theif2.to_string())

```

### List 형태의 JSON 로딩
```python
import json

with open('data/girlgroup.json', 'w') as fp:
    data = '[ "소녀시대", "앱터스쿨", "에이핑크", "걸스데이", "우주소녀" ]'
    fp.write(data)

with open('data/girlgroup.json') as data_file:
    girlgroup = json.load(data_file)

print(girlgroup)
print(type(girlgroup))

print('-'*50)
# 출력 : 내가 좋아하는 걸그룹은 에이핑크와 우주소녀입니다.
text = "내가 좋아하는 걸그룹은 {}와 {}입니다.".format(
    girlgroup[2], girlgroup[4]
)
print(text)

```

### Dict 형태의 JSON 로딩
```python
import json

data = '''
    {
        "name" : "홍길동",
        "age"  : 20,
        "addr" : {
            "city"  : "서울시",
            "dong"  : "월계동"
        }
    }
'''
with open('data/member.json', 'w') as fp:
    fp.write(data)

with open('data/member.json') as data_file:
    member = json.load(data_file)

print(member)
print(type(member))

print('-'*50)
# 출력 : 홍길동은 20살 이고, 서울시 염창동에 살고 있습니다.
text = "{}은 {}살 이고, {} {}에 살고 있습니다.".format(
    member["name"],
    member["age"],
    member["addr"]["city"],
    member["addr"]["dong"],
)
print(text)
```

### QUIZ
```python
import json

data = '''
{
    "name" : "홍길동",
    "dog"  : {
        "name" : "순둥이",
        "toys" : [
                { "name" : "뽀로로" },
                { "name" : "토마스" }
        ]
    }
}
'''

with open('data/person.json', 'w') as fp:
    fp.write(data)

with open('data/person.json') as data_file:
    person = json.load(data_file)

print(person)
print(type(person))

print('-'*50)
# 출력 : 홍길동의 개 순둥이의 장난감은 뽀로로, 토마스입니다.
text = "{}의 개 {}의 장난감은 {}, {}입니다.".format(

)
print(text)

```


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
