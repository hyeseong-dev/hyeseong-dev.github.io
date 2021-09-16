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

