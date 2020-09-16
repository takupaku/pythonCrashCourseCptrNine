class User:
    def __init__(self,first_name,last_name,location,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.gender=gender

    def describe_user(self):
        print("The user "+self.first_name.title()+" "+self.last_name.title()+" lives in "+self.location.title()+" and is a "+self.gender)

    def greet_user(self):
        print("Assalamualaikum "+self.first_name+" "+self.last_name+"\n")

class Admin(User):
    def __init__(self,first_name,last_name,location,gender):
        self.priviledges=['can add post','can delete post','can ban user']
        super().__init__(first_name,last_name,location,gender)
        #self.priviledgess=Privileges()#using privilige class as a attribute
    def show_priviledge(self):
        for privilege in self.priviledges:
            print('you '+ privilege)
        print('if done, press OK')


admin=Admin('Ryoma','Echizen','Japan','male')
admin.describe_user()
admin.greet_user()
admin.show_priviledge()

'''creating instance after using Privilege class as attribute(This class updated show_privilige method)'''
#new_instance=Admin()
#new_instance.priviledgess.show_priviledge()

