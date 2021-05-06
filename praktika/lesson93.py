
class User():
    """ Создания личных дел User  """

    def __init__(self, first_name, last_name, age):
        """Создания основныее отрибуты User вод (имени, фомилии, возраст)"""
        self.first_name = first_name
        self.last_name =last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """личное дело User"""
        print(
            "User: " + self.first_name + ' ' + self.last_name +  " " + str(self.age) +
            "\nЛичное Дело: \n В полном обеме выполняет поставленые задачи, имеет склонность "
            "к антипалетичной деятельности против власти, был замечен в деятельности против пропаганды гос сми."
            " \nРекомендация к работе: Не допускать к руководящим должностям!!\n"
              )

    def user_info(self):
        print(self.last_name + ' ' + self.first_name + ' ' + str(self.age))

    def greet_user(self):
        print("Добро пожаловать в наш колектив: " + self.first_name + "\n")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print(self.login_attempts)


