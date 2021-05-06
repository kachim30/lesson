from lesson93 import User

"""Создаем администратара на базе класса User с добавлением новых функций"""
class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.administrator_Prov = []


    def prov(self, popa):
        self.administrator_Prov += popa

    def show_privileges(self):
        print(self.administrator_Prov)

es = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей' ]
admin_Bil = Admin("Ilya", 'veretsenntikau', 34)
admin_Bil.prov(es)

admin_Bil.user_info()
admin_Bil.show_privileges()





