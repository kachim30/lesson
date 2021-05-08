from lesson93 import User




"""Создаем администратара на базе класса User с добавлением новых функций"""
class Admin(User):

    def __init__(self, first_name, last_name, age, ):
        super().__init__(first_name, last_name, age)
        self.administrator_Prov = []

    def user_info(self):
        print(self.last_name + ' ' + self.first_name + ' ' + str(self.age) + "\nСписок привелегий:  " + str(self.administrator_Prov))

    def list_privileges(self, list_p):
        for x in list_p:
            self.administrator_Prov.append(x)

    def print_privileges(self):
        print(self.administrator_Prov)



es = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей' ]






er = ('разрешено добавлять сообщения', 'разрешено удалять пользователей', 'разрешено банить пользователей')

admin_gom = Admin("Gom", "vert", 32)
admin_gom.list_privileges(es)
admin_gom.user_info()

