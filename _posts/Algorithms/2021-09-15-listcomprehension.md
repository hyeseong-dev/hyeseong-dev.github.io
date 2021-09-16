# 2.4.3 리스트 컴프리헨션  
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


## 리스트 컴프리헨션의 좋은 예 VS 나쁜 예


```python
result = []
for x in range(10):
    for y in range(5):
        if x * y > 10:
            result.append((x,y))
```


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

```
