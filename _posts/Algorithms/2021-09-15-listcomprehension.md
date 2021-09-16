# 리스트 컴프리헨션  
리스트 컴프리헨션은 반복문의 표현식(조건 포함 가능)

__- [ 항목 for 항목 in 반복 가능한 객체]__  
__- [ 표현식 for 항목 in 반복 가능한 객체]__  
__- [ 표현식 for 항목 in 반복 가능한 객체 if 조건문]__  




```python
a = [y for y in range(1900, 1940) if y%4 ==0 ]
print(a)
```

    [1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936]



```python
b = [2**i for i in range(13)]
print(b)

```

    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]



```python
c = [x for x in a if x%2==0]
c
```




    [1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936]




```python
d = [str(round(335/113.0, i)) for i in range(1,6)]
d
```




    ['3.0', '2.96', '2.965', '2.9646', '2.9646']




```python
words = 'Buffy is awesome and a vampire slayer'.split()
e = [[w.upper(), w.lower(), len(w)]for w in words]
e
```




    [['BUFFY', 'buffy', 5],
     ['IS', 'is', 2],
     ['AWESOME', 'awesome', 7],
     ['AND', 'and', 3],
     ['A', 'a', 1],
     ['VAMPIRE', 'vampire', 7],
     ['SLAYER', 'slayer', 6]]




```python
for i in e:
    print(i)
    
```

    ['BUFFY', 'buffy', 5]
    ['IS', 'is', 2]
    ['AWESOME', 'awesome', 7]
    ['AND', 'and', 3]
    ['A', 'a', 1]
    ['VAMPIRE', 'vampire', 7]
    ['SLAYER', 'slayer', 6]


# 리스트 컴프리헨션의 좋은 예

##  좋은 예



```python
result = []
for x in range(10):
    for y in range(5):
        if x * y > 10:
            result.append((x,y))

for x in range(5):
    for y in range(5):
        if x != y:
            for z in range(5):
                if y != z:
                    yield(x, y, z)

return ((x, complicated_transform(x))
    for x in long_generator_function(parameter)
    if x is not None)

squares = [x * x for x in range(10)]

eat(jelly_bean for jelly_bean in jelly_beans if jelly_bean.color == 'black')

result = [(x,y) for x in range(10) for y i n range(5) if x * y > 10]

return ((x, y, z))
        for x in xrange(5)
        for y in xrange(5)
        if x != yfor z in xrange(5)
        if y != z)
```


      File "/tmp/ipykernel_330/2161323672.py", line 22
        result = [(x,y) for x in range(10) for y i n range(5) if x * y > 10]
                                                 ^
    SyntaxError: invalid syntax



## 리스트 메서드 성능 측정

리스트의 메서드를 벤치마킹 테스트하여 성능을 측정해보자. 아래 테스트에서는 timeit 모듈의 Timer 객체를 생성해 사용. 
Timer 객체의 첫 번째 매개변수는 우리가 측정하고자 하는 코드이며, 두 번째 매개변수는 테스트를 위한 설정 문이다. timeit 모듈은 명령문을 정해진 횟수만큼 실행하는 데 걸리는 시간을 측정한다.(기본값은 number = 1000000이다). 테스트가 완료되면, 문장이 수행된 시간(밀리초)을 부동소수점 값으로 반환한다. 



```python
# 2_runtime_lists_with_timeit_module.py
# timeit() 메서드로 성능을 측정할 때는 임시로 가비지 컬렉션 기능이 중진된다. 가비지 컬렉션 수행 시간도 성능 측정에 같이 포함하고 싶다면, 다음과 같이 gc.enable()를 추가해야 한다. 


def test1():
    l = []
    for i in range(1000):
        l = l + [i]

def test2():
    l = list()
    for i in range(1000):
        l.append(i)

def test3():
    l = list(i for i in range(1000))

def test4():
    l = list(range(1000))


if __name__ == '__main__':
    import timeit
    t1 = timeit.Timer("test1()", "from __main__ import test1")
    print('concat', t1.timeit(number=1000), 'milliseconds')
    t2 = timeit.Timer("test2()", "from __main__ import test2")
    print('append', t2.timeit(number=1000), 'milliseconds')
    t3 = timeit.Timer("test3()", "from __main__ import test3")
    print('comprehension', t3.timeit(number=1000), 'milliseconds')
    t4 = timeit.Timer("test4()", "from __main__ import test4")
    print('list range', t4.timeit(number=1000), 'milliseconds')



```

    concat 1.8474249999999302 milliseconds
    append 0.05421500000011292 milliseconds
    comprehension 0.0399293000009493 milliseconds
    list range 0.016438300001027528 milliseconds



```python
result
```




    [(3, 4),
     (4, 3),
     (4, 4),
     (5, 3),
     (5, 4),
     (6, 2),
     (6, 3),
     (6, 4),
     (7, 2),
     (7, 3),
     (7, 4),
     (8, 2),
     (8, 3),
     (8, 4),
     (9, 2),
     (9, 3),
     (9, 4)]



#


```python
# 문자열 단어 단위로 반전
def reverser(string1, p1=0, p2=None):
    length= len(string1)
    if length < 2:        # 2개문자 미만일 경우 예) '안', '뭐', ' ', '1'
        return string1
                          # p2의 경우에는 3번째 매개변수가 존재할 경우, 전체문장에서 각 공백간 구분된 단어의 마지막 인덱스를 의미 length는 문장의 길이를 의미
    p2 = p2 or length-1   # 두 번째 포인터가 존재하거나 또는 string1이 2단어 이상일 때  / 예) "재미있다. 정말 알고리즘 파이썬"의 경우 전체길이가 17이고 이를 -1로 빼서 p2는 16이됨
    while p1 < p2:        # p1 포인터가 항상 p2보다 작은 경우 돌아감 , p2는 16 , p1은 0
        string1[p1], string1[p2] = string1[p2], string1[p1] # 처음 string1[p2]의 == '.' , string1[p1] == '파' 
        p1 += 1                                             # p1 = 2 변경
        p2 -= 1                                             # p2 = 15 변경
    
def reversing_words_sentence_logic(string1): # 매개변수['파','이','썬',' ' ,'정','말', '재','미','있','다','.']
    # 먼저, 문장 전체를 반전함.
    reverser(string1)                       
    print(string1)  # ['.', '다', '있', '미', '재', ' ', '말', '정', ' ', '즘', '리', '고', '알', ' ', '썬', '이', '파'] 
    p = 0
    start = 0
    while p < len(string1):
        if string1[p] == u"\u0020":
            # 단어를 다시 반전한다(단어를 원위치로 돌려놓는다.)
            reverser(string1, start, p-1) # start는 ['.', '다', '있', '미', '재'] 리스트에서 '.'의 인덱스 0에 해당하고 p-1은 '재'에 해당하는 '4'에 해당
            print(string1)
            start = p+1
        p += 1
    # 마지막 단어를 반전한다(단어를 원위치로 돌려놓는다.)
    reverser(string1, start, p-1)
    return ''.join(string1)

if __name__ == '__main__':
    str1 = '파이썬 알고리즘 정말 재미있다.'
    str2 = reversing_words_sentence_logic(list(str1))
    print(str2)
```

    ['.', '다', '있', '미', '재', ' ', '말', '정', ' ', '즘', '리', '고', '알', ' ', '썬', '이', '파']
    ['재', '미', '있', '다', '.', ' ', '말', '정', ' ', '즘', '리', '고', '알', ' ', '썬', '이', '파']
    ['재', '미', '있', '다', '.', ' ', '정', '말', ' ', '즘', '리', '고', '알', ' ', '썬', '이', '파']
    ['재', '미', '있', '다', '.', ' ', '정', '말', ' ', '알', '고', '리', '즘', ' ', '썬', '이', '파']
    재미있다. 정말 알고리즘 파이썬


# 하나의 반복문으로 반전





```python
def reverse_words_brute(string):
    word, sentence = list(), list()
    for character in string:
        if character != ' ':
            word.append(character)
        else:
            # 조건문에서 empty list is False, 여러 공백이 있는 경우, 조건문을 건너뜀
            if word:
                sentence.append(''.join(word))
            word = list() # word 리스트를 초기화 함
    
    # 마지막 단어가 있다면, 문장에 추가 
    if word != '':
        sentence.append(''.join(word)) # word 변수의 각각 파편화된 문자를 단어로 변경하여 sentence 리스트 뒤에 붙여버림
    sentence.reverse()                 # 최종적으로 단어들이 담긴 리스트['파이썬', '알고리즘', '정말', '재미있다.']를 reverse메서드를 이용하여 원본값을 변경시킴
    return ' '.join(sentence)

if __name__ == '__main__':
    str1 = '파이썬 알고리즘 정말 재미있다.'
    str2 = reverse_words_brute(list(str1))
    print(str2)


```

    재미있다. 정말 알고리즘 파이썬


# 문자열을 공백으로 구분하여 리스트를 생성한 다음, 슬라이스를 사용



```python
def reversing_words_slice(word):
    new_word = []
    words = word.split(" ")
    for word in words[::-1]:
        new_word.append(word)
    return ' '.join(new_word)

if __name__ == '__main__':
    str1 = '파이썬 알고리즘 정말 재미있다'
    str2 = reversing_words_slice(str1)
    print(str2)
```

    재미있다 정말 알고리즘 파이썬


아예 반복문 없이 리스트와 문자열 메서드만으로 해결할 수도 있다. 


```python
# 7_reversing_words.py

def reversing_words(str1):
    words = str1.split(' ')
    rev_set = ' '.join(reversed(words))
    return rev_set

def reversing_words2(str1):
    words = str1.split(' ')
    words.reverse()
    return ' '.join(words)

if __name__ == '__main__':
    str1 = '파이썬 알고리즘 정말 재미있다'
    str2 = reversing_words(str1)
    str3 = reversing_words2(str1)
    print(str2)
    print(str3)

```

    재미있다 정말 알고리즘 파이썬
    재미있다 정말 알고리즘 파이썬


위 문제를 조금 더 확장하면 ! ? ; - . 등의 기호를 구분자로 사용하는 코드도 만들 수 있을 것이다.

# 단순 문자열 압축

다음은 문자열 aabcccccaaa를 a2b1c5a3 같은 형식으로 압축하는 예제다. 



```python
# 8_simple_str_compression.py

def str_compression(s):
    count, last = 1, ''
    list_aux = list()
    for i, c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            count = 1
            last = c
    list_aux.append(str(count))
    return ''.join(list_aux)

if __name__ == '__main__':
    result = str_compression('aabcccccaaa')
    print(result)
```

    a2b1c5a3


# 회문

회문이란 앞에서부터 읽으나 뒤에서부터 읽으나 동일한 단어나 구를 뜻한다. 어떤 문자열이 회문인지 확인하는 코드를 작성해보자. 공백은 무시하며, 세가지 버전으로 구현했음



```python
# 11_palindrome.py

str1 = '다시 합창합시다'
str2 = ''
str3 = 'hello'

def is_palindrome(s):
    l = s.split(' ')
    s2 = ''.join(l)
    return s2 == s2[::-1]

def is_palindrome2(s):
    l = len(s)
    f, b = 0, l-1
    while f < l //2:
        while s[f] == ' ':
            f+=1
            while s[b] == ' ':
                b -=1
            if s[f] != s[b]:
                return False
            f+=1
            b-=1
        return True


def is_palindrome3(s):
    s = s.strip()  # 양쪽 공백 모두 제거
    if len(s) < 2: # 한 글자인 경우 palindrome : True
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


print(is_palindrome(str1))
print(is_palindrome(str2))
print(is_palindrome(str3))
print()
print(is_palindrome2(str1))
print(is_palindrome2(str2))
print(is_palindrome2(str3))
print()
print(is_palindrome3(str1))
print(is_palindrome3(str2))
print(is_palindrome3(str3))



```

    True
    True
    False
    
    True
    None
    True
    
    True
    True
    False



```python

```




    4.0




```python

```
