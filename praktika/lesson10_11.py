import json


first_name = input("Введите имя для проверки есть ли пользователь в базе данных:\n")
first_name2 = first_name.title()

def verifcationUser():
    """Проверка пользователя на наличие созданного файла. А также внесения дополнений, создания и просмотра файлов."""
    try:
        with open(first_name2) as x:
            print("Существует пользователь: " + first_name2 + "\n Желаете внести дополнительные данные в файл пользователя Yes or No?\n")
            question = input().title()

            if  question == "Yes":
                userChangesInData()
            elif question == "No":
                print("Желаете просмотреть данные в файле пользователя Yes or No?\n")
                question2 = input().title()
                if question2 == "Yes":
                    userNamberInfo()
                elif question2 == 'No':
                    print("Хорошего дня!")
    except FileNotFoundError:
        print("Пользователь не найден: " + first_name + "\n Желаете создать пользователя? Yes or No\n")
        question1 = input().title()

        if question1 == "Yes":
            userCreation()
        elif question1 == "No":
            print("Хорошего дня!")

def userChangesInData():
    """Добавление данных о пользователе."""
    try:
        with open(first_name2, "a") as ys:
            infoUser = input("Введите данные:\n")
            json.dump(infoUser, ys)
            print("Данные в ведены. Не желаете просмотреть введенные дополнения? Yes or No?\n")
            question3 = input().title()

            if question3 == "Yes":
                userNamberInfo()
            elif question3 == "No":
                print("Хорошего дня!")
    except FileNotFoundError:
        print("Некорректные данные.")

def userCreation():
    """Создание нового пользователя."""

    with open(first_name2, 'w') as nm:
        json.dump(first_name2, nm)
        print('Создан пользователь: ' + first_name2)

def userNamberInfo():
    """Получения данных о пользователе."""
    try:
        with open(first_name2, 'r') as name1:
            nameinfo = name1.read()
            print("На ваш запрос выведена информация файла:\n " + nameinfo)
    except FileNotFoundError:
        print("Неверные данные.")




verifcationUser()