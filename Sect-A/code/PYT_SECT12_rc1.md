
# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, 김진수</font></div>
<hr>

## <font color='brown'>입/출력 그리고 로깅</font>
>
- 포맷을 위한 문자열행 메소드. format( )
- 다양한 포맷에 대한 예제
- 로깅(Logging)의 이해
- 로깅 라이브러리 사용법
- 로깅 제대로 사용하기
- 설정 파일을 활용한 로깅


### 로깅(Logging) 예제1


```python

import logging

t_debug = logging.debug('분석')
t_info  = logging.info('확인')
t_warn  = logging.warning('경고')
t_error = logging.error('에러')
t_critic= logging.critical('심각')

print("{} : {}".format("1단계", t_debug))
print("{} : {}".format("2단계", t_info))
print("{} : {}".format("3단계", t_warn))
print("{} : {}".format("4단계", t_error))
print("{} : {}".format("5단계", t_critic))
```


### 로깅(Logging) 예제2


```python

import logging

logging.basicConfig(filename='log/basic_mode.log', encoding='utf-8', level=logging.DEBUG)

logging.debug('디버깅모드에서 프로그램 진단')
logging.info('예상대로 작동하는지에 대한 확인')
logging.warning('예상하지 못한 문제가 발생')
logging.error('프로그램 오류로 인해 SW기능이 제대로 수행하지 못함')
logging.critical('심각한 에러로 즉각적인 대응이 요구')

```

### 로깅(Logging) 예제3


```python
import logging
import test_lib

logging.basicConfig(filename='log/test_mode.log', level=logging.INFO, encoding='utf-8')

def main():
    logging.info('메인함수 시작')
    test_lib.do_something()
    logging.info('메인함수 종료')

if __name__ == '__main__':
    main()

```

- test_lib.py

```python
# test_lib.py
import logging

def do_something():
    logging.info('Doing something')

```


### 로깅(Logging) 예제4


```python
import logging

# levelname(심각도), message(이벤트설명)

# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
# logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)

level=logging.DEBUG
logging.basicConfig(format='%(levelname)s:%(message)s', level=level)

logging.debug('   [1단계] 디버깅 메시지')
logging.info('    [2단계] 정보성 메시지')
logging.warning(' [3단계] 경고성 메시지')
logging.error('   [4단계] 에러성 메시지')
logging.critical('[5단계] 심각한 메시지')


```

### 로깅(Logging) 예제5


```python
import logging

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning('기본형 날짜시간 정보 추가')

```


```python
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('포맷형 날짜시간 정보 추가')

```


```python
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y.%m.%d %I:%M:%S %p')
logging.warning('포맷형 날짜시간 정보 추가')

```


```python
import logging

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y.%m.%d %I:%M:%S %a')
logging.warning('포맷형 날짜시간 정보 추가')

```

### 로깅(Logging) 예제6


```python
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y.%m.%d %I:%M:%S %p')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

```

### 로깅(Logging) 예제7


```python
import logging.config

logging.config.fileConfig('config/logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

```

- config/logging.conf
```python
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
# datefmt=%Y.%m.%d %I:%M:%S %p

```


<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
