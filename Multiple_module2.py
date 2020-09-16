from Multiple_module1 import  User
class Privileges():
    def __init__(self):
        self.privilideges=['update','delete','insert']

    def show_priviledge(self):
        for privilidege in self.privilideges:
            print(privilidege)


class Admin(User):
    def __init__(self, first_name, last_name, location, gender):
        super().__init__(first_name, last_name, location, gender)
        self.priviledges = ['can add post', 'can delete post', 'can ban user']

        self.priviledgess = Privileges()  # using privilige class as a attribute