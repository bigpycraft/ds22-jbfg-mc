# Industry 4.0 의 중심, BigData

<div align='right'><font size=2 color='gray'>Data Processing Based Python @ <font color='blue'><a href='https://www.facebook.com/jskim.kr'>FB / jskim.kr</a></font>, [김진수](bigpycraft@gmail.com)</font></div>
<hr>

## <font color='brown'>Python Practice </font>
> 과제명 : 모양그리기   
- 주어진 모양을 최소한의 코드로 그려보기
- Hint : 대각선 길이를 구하는 제곱근 (Root Square)

``` python
import math

diagonal = math.sqrt(width**2 + height**2)

```

### Exemple Code


```python
import turtle
import math

input('[Enter]키를 클릭하면 그림을 그립니다... ')

turtle.color('red')
turtle.pensize(5)
width  = 300
height = width
diagonal = math.sqrt(width**2 + height**2)

turtle.forward(width)
turtle.left(90)
turtle.forward(height)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(height)

turtle.left(135)
turtle.forward(diagonal)
turtle.left(90)
turtle.forward(diagonal/2)
turtle.left(90)
turtle.forward(diagonal/2)
turtle.left(90)
turtle.forward(diagonal)

turtle.done()
```

    [Enter]키를 클릭하면 그림을 그립니다... 
    

<hr>
<marquee><font size=3 color='brown'>The BigpyCraft find the information to design valuable society with Technology & Craft.</font></marquee>
<div align='right'><font size=2 color='gray'> &lt; The End &gt; </font></div>
