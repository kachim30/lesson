
tex = "lesson10_1.xtx"


with open(tex) as did:
    """Вывод текста"""
    for lines in did.readlines():
        print(lines.rstrip())




with open(tex) as ddd:
    """Вывод текста и замена слова """
    for ler in ddd:
        print(ler.replace('Python', 'C').rstrip())






