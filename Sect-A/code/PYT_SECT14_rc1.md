
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>OS 모듈</font>
>  
- 파일/디렉토리 관련 Command 구현



### 파일 I/O


```python
def write_txt(filepath):
    # 텍스트 파일에 한줄씩 쓰기(writelines)
    count = 1
    data = []
    print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')

    while True:
        text = input('[%d] 파일에 저장할 내용을 입력하세요: ' % count)
        if text == '':
            break
        data.append(text + '\n')
        count += 1

    f = open(filepath, 'w')
    f.writelines(data)
    f.close()

    ret = 'TEXT 파일을 생성하였습니다.'

    return ret


# 파일 생성
filepath = './data/mydata.txt'
# write_txt(filepath)

# 파일 읽기
f = open(filepath, 'r')
data = f.read()
f.close()

print(data)

```

### 텍스트 파일 복사
```python
# 텍스트 파일 복사하기(read, write)
f = open('./data/mydata.txt', 'r')
h = open('./data/mydata_copy.txt', 'w')

data = f.read()
h.write(data)

h.close()
f.close()

with open('./data/mydata_copy.txt', 'r') as fp:
    data = fp.read()

print(data)
```

### Image 파일 복사
```python
# Image 파일 복사
origin_img = './images/bpc_logo.png'
copied_img = './images/bpc_logo_copy.png'

# 바이너리 파일 복사하기(read, write)
bufsize = 2**10    # 1KB, 1024
f = open(origin_img, 'rb')
h = open(copied_img, 'wb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)

h.close()
f.close()


```

### 파일 크기 구하기
```python
# 파일 크기 구하기(ospathgetsize)
from os.path import getsize

file1 = './data/mydata.txt'
file2 = './images/company_logo.png'

# OK !!
# file2 = '/Users/user/Dropbox/sect_tech/src_anaconda/images/company_logo.txt.png'

# SyntaxError
# file2 = 'C:\Users\user\Dropbox\sect_tech\src_anaconda\images\company_logo.png'

file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name: %s \t File Size: %d Byte' %(file1, file_size1))
print('File Name: %s \t File Size: %d Byte' %(file2, file_size2))
```

### 파일 삭제하기
```python
# 파일 삭제하기(osremove)
from os import remove

target_file = './data/mydata_copy.txt'
k = input('[%s] 파일을 삭제하겠습니까? ([y]/n)' %target_file)

if k == 'y' or k == '':
    remove(target_file)
    print('[%s] 파일을 삭제했습니다.' %target_file)

```

### 파일이름 바꾸기
```python
# 파일이름 바꾸기(osrename)
from os import rename

folder_path = './data/'
target_file = folder_path + 'mydata.txt'
newname = input('[%s]에 대한 새로운 파일 이름을 입력하세요: ' %target_file)

# new_file = folder_path + newname
new_file = newname
rename(target_file, new_file)
print('[%s] -> [%s] 로 파일이름이 변경되었습니다.' %(target_file, new_file))
```

### 디렉터리에 있는 파일목록 얻기
```python
# 디렉터리에 있는 파일목록 얻기(os.listdir, glob.glob)
import os, glob

folder = 'C:\Temp'
# folder = 'data'
file_list1 = os.listdir(folder)
print(file_list1)

# files = '*.txt'
files = 'data/*.txt'
file_list2 = glob.glob(files)
print(file_list2)
```

### 현재 디렉터리 확인하고 바꾸기
```python
# 현재 디렉터리 확인하고 바꾸기(os.getcwd, os.chdir)
import os
import time

pdir = os.getcwd();
print(pdir)
time.sleep(1)

os.chdir('data');
print(os.getcwd())
time.sleep(1)

os.chdir('..');
print(os.getcwd())
time.sleep(1)

os.chdir(pdir);
print(os.getcwd())
```

### 디렉터리 생성하기
```python
# 디렉터리 생성하기(osmkdir)
import os

newfolder = input('새로 생성할 디렉터리 이름을 입력하세요: ')

try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리를 새로 생성했습니다.' %newfolder)
except Exception as e:
    print(e)
```

### 디렉터리 제거하기
```python
# 디렉터리 제거하기(osrmdir)
import os

# target_folder = newfolder
target_folder ='atemp'

k = input('[%s] 디렉터리를 삭제하겠습니까? (y/n)' %target_folder)
if k == 'y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제했습니다.' %target_folder)
    except Exception as e:
        print(e)
```

### 하위 디렉터리 및 파일 전체 삭제하기
```python
# 하위 디렉터리 및 파일 전체 삭제하기(shutil.rmtree)
import shutil
import os

target_folder = 'E:/devlab/tmp'
print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.' %target_folder)

for file in os.listdir(target_folder):
    print(file)
k = input('[%s]를 삭제하겠습니까? (y/n) ' %target_folder)

if k == 'y':
    try:
        shutil.rmtree(target_folder)
        print('[%s]의 모든 하위 디렉터리와 파일들을 삭제했습니다.' %target_folder)
    except Exception as e:
        print(e)
```

### 파일이 존재하는지 체크하기
```python
# 파일이 존재하는지 체크하기(os.pathexists)
import os
from os.path import exists

dir_name = input('새로 생성할 디렉터리 이름을 입력하세요: ')

if not exists(dir_name):
    os.mkdir(dir_name)
    print('[%s] 디렉터리를 생성했습니다.' %dir_name)
else:
    print('[%s]은(는) 이미 존재합니다.' %dir_name)

```

### 파일인지 디렉터리인지 확인하기
```python
# 파일인지 디렉터리인지 확인하기(os.pathisfile, os.pathisdir)
import os
from os.path import exists, isdir, isfile

# files = os.listdir('..')
files = os.listdir()
# print('files :', files)

for file in files:
    if isdir(file):
        print('<DIR> %s' %file)

for file in files:
    if isfile(file):
        print('FILE : %s' %file)
```

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
