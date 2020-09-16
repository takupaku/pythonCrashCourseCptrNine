class User:
    def __init__(self,first_name,last_name,location,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.gender=gender
        self.login_attemps=0

    def describe_user(self):
        print("The user "+self.first_name.title()+" "+self.last_name.title()+" lives in "+self.location.title()+" and is a "+self.gender)

    def greet_user(self):
        print("Assalamualaikum "+self.first_name+" "+self.last_name+"\n")

    '''method to increment login attempt'''
    def increment_login_attempts(self,atmpt=1):
        self.login_attemps+=atmpt

    '''resets the login attempt to 0'''
    def reset_login_attempts(self,reset=0):
        self.login_attemps=reset


first_user = User("Takwa","Shahidi","Uttara","Female")
second_user = User("Echizen","Ryoma","Nagoya","Male")
third_user = User("Aysha","Ferdaus","Syria","Female")

first_user.describe_user()
first_user.greet_user()

second_user.describe_user()
second_user.greet_user()

third_user.describe_user()
third_user.greet_user()

'''incrementing user's login_attempts'''
first_user.increment_login_attempts()
first_user.increment_login_attempts()
print(first_user.login_attemps)

second_user.increment_login_attempts()
print(second_user.login_attemps)

'''resetting login_attempts value to 0 by calling reset_login_attempts method'''
first_user.reset_login_attempts()
print(first_user.login_attemps)
