x = True
while x :
    try:
        nev = input('Для завершения введите "q" чтобы начать сложения нажмите Entra:\n')
        if nev == 'q':
            break
        number = number1 = int(input("Введите цифру 1: ")) + int(input("Введите цифру 2 :"))


        print(number)
    except ValueError:
        msg = "Буквы нельзя вводить только цифры!"
        print(msg)


