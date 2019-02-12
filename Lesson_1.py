"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
также проверить тип и содержимое переменных.
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в
строковый тип на кириллице.
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
phrases = ['разборка', 'сокет', 'декоратор']
print('строковый формат:')
for i in range(0,len(phrases)):
    print(phrases[i])
print('типы строкового отображения:')
for i in range(0,len(phrases)):
    print(type(phrases[i]))

phrases_unic =['\u0440\u0430\u0437\u0431\u043E\u0440\u043A\u0430','\u0441\u043E\u043A\u0435\u0442',
               '\u0434\u0435\u043A\u043E\u0440\u0430\u0442\u043E\u0440']
for i in range(0,len(phrases_unic)):
    print(phrases_unic[i])
for i in range(0,len(phrases_unic)):
    print(type(phrases_unic[i]))

print('----------------------------------------------------------------------------------------------')

phrases = [b'class', b'function', b'method']
print('байтовый формат:')
for i in range(0,len(phrases)):
    print(phrases[i])
print('типы строкового отображения:')
for i in range(0,len(phrases)):
    print(type(phrases[i]))
print('----------------------------------------------------------------------------------------------')
phrases = ['attribute', 'класс', 'функция', 'type']
for i in range(0,len(phrases)):
    temp = b'%a' % phrases[i]
    print(temp)
    print(type(temp))
#
print('----------------------------------------------------------------------------------------------')
phrases = ['разработка', 'администрирование', 'protocol', 'standard']
for i in range(0,len(phrases)):
    enc = phrases[i].encode('utf-8')
    dec = bytes.decode(enc, encoding='utf-8')
    print('encode: ', enc, ' decode: ', dec)

print('----------------------------------------------------------------------------------------------')
import subprocess

prearg = ['yandex.ru', 'youtube.com']
for i in range(len(prearg)):
    args = ['ping', prearg[i]]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
    # выводим результат в байтах
        print(line)

    # изменяем кодировку результата
        line = line.decode('cp866').encode('utf-8')
    # выводим результат в кодировке utf-8
        print(line.decode('utf-8'))
print('----------------------------------------------------------------------------------------------')
import locale

f_n = open('test.txt', 'w')
f_n.write('сетевое программирование, сокет, декоратор')
f_n.close()
print(type(f_n))

with open('test.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')
#получаем ошибку