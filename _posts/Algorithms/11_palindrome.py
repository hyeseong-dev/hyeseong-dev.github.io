# 11_palindrome.py

# def is_palindrome(s):
#     l = s.split(' ')
#     s2 = ''.join(l)
#     return s2 == s2[::-1]

# def is_palindrome2(s):
#     l = len(s)
#     f, b = 0, l-1
#     while f < l //2:
#         while s[f] == ' ':
#             f+=1
#         while s[b] == ' ':
#             b -=1
#         if s[f] != s[b]:
#             return False
#         f+=1
#         b-=1
#     return True

str1 = '다시 합창합시다'
str2 = ''
str3 = 'hello'

# print(is_palindrome2(str1))
# print(is_palindrome2(str2))
# print(is_palindrome2(str3))


def is_palindrome3(s):
    s = s.strip()  # 양쪽 공백 모두 제거
    if len(s) < 2: # 한 글자인 경우 palindrome : True
        return True
    if s[0] == s[-1]:
        return is_palindrome3(s[1:-1])
    else:
        return False

print()
print(is_palindrome3(str1))
print(is_palindrome3(str2))
print(is_palindrome3(str3))
