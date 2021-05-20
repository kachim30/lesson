
"""файлы к lesson идут 'cats.txt', 'dogs.txt' """

def count_words(filename):
    """Вывод текста файлов"""
    try:
        with open(filename) as x:
            contents = x.read()
            print(contents.rstrip())
    except FileNotFoundError:
        msg = 'Вы неправильно указали файл для открытия'
        pass


x = True

while x:
    """зацикливания ввода адресов файлов"""
    ip = input('Адрес файла для открытия:\n')
    if ip == 'q':
        break
    else:
        count_words(ip)