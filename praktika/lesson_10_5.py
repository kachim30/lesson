
with open('lesson10_5.txt', 'a') as gus:
    """Закрытия опроса 'q' Опрос  и сохранение в файл lesson10_5.txt"""
    while gus:
        xs = str(input('Ваше имя?\n'))

        if xs  == "q":
            break
        else:
            sx = str(input('Почему вам нравиться программировать?\n'))
            gus.write('Имя гостя: ' + xs + '\n' + "Причина: " + sx + "\n")


with open('lesson10_5.txt', 'r') as x:
    """Выводит содержимое файла lesson10_5.txt"""
    for ler in x:
        print(ler.rstrip())





