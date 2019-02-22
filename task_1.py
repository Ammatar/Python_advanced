"""
1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
"""
import hashlib

#S = str.lower(input('Введите строку(только латинские буквы): '))
S = "asa"

def subs(S):
    count_subs = set()
    for i in range(len(S) + 1):
        for j in range(i + 1, len(S) + 1):
            sub = hashlib.sha1(S[i:j].encode('utf-8')).hexdigest()
            count_subs.add(sub)
        #print(count_subs)
        return len(count_subs)


print(subs(S))
print(f'В строке {S} содержится {subs(S)} подстрок.')
