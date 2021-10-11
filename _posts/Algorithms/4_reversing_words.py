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
            print(p-1,'p-1')
            reverser(string1, start, p-1) # start는 ['.', '다', '있', '미', '재'] 리스트에서 '.'의 인덱스 0에 해당하고 p-1은 '재'에 해당하는 '4'에 해당
            print(string1)
            start = p+1
        p += 1
    # 마지막 단어를 반전한다(단어를 원위치로 돌려놓는다.)
    reverser(string1, start, p-1)
    print(string1)
    return ''.join(string1)

if __name__ == '__main__':
    str1 = '파이썬 알고리즘 정말 재미있다.'
    str2 = reversing_words_sentence_logic(list(str1))
    print(str2)