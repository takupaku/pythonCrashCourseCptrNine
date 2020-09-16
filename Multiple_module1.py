class User:
    def __init__(self , first_name ,last_name,location,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.location=location
        self.gender=gender

    def describe_user(self):
        print("The user "+self.first_name.title()+" "+self.last_name.title()+" lives in "+self.location.title()+" and is a "+self.gender)

    def greet_user(self):
        print("Assalamualaikum "+self.first_name+" "+self.last_name+"\n")