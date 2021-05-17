



with open('guest.txt', 'a') as gus:
    """Запрашивает имя гостя и сохраняет в файл guest.txt"""
    while gus:
        xs = str(input('Ваше имя?\n'))
        if xs == "q":
            break
        else:
            gus.write('Имя гостя: ' + xs + '\n')


with open('guest.txt', 'r') as x:
    """Выводит содержимое файла guest.txt"""
    for ler in x:
        print(ler.rstrip())
