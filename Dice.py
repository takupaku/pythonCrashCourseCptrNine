from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides


    def roll_die(self):
        x=randint(1,self.sides)
        return x

print("-------First turn-----------")
lists=[]
die1=Die()
for roll_no in range(10):
    result=die1.roll_die()
    lists.append(result)
print(lists)


lists=[]
print("--------Second turn---------")
die2=Die(10)
for roll_no in range(10):
    result=die2.roll_die()
    lists.append(result)

print(lists)


lists=[]
print("----------Third turn--------")
die2=Die(20)
for roll_no in range(10):
    result=die2.roll_die()
    lists.append(result)

print(lists)





