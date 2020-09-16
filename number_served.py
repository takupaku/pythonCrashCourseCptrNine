class Restaurant():
    '''simple attempt to represent restaurant'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name#attribute
        self.cuisine_type=cuisine_type
        self.number_served=0#default value

    def describe_restaurant(self):
        print("The restaurant is called "+self.restaurant_name.title())
        print("Type of the restaurant is  "+self.cuisine_type.title())#'cuisine_type.title' only wont work,one must pass self in method and use it

    def open_restaurant(self):
        print("the restaurant "+self.restaurant_name+" is opened!!")

    '''setting new number through updating attribute value'''
    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, new_guest):
        self.number_served += new_guest




restaurant = Restaurant("Azo idea space", "Fine dinning")
print(restaurant.restaurant_name)#printing each attribute
print(restaurant.cuisine_type)
restaurant.describe_restaurant()#calling method from the class
restaurant.open_restaurant()

#---------the main starts here--------
print(restaurant.number_served)# Current attribute vavlu / default attribute

'''setting new number through updating attribute value'''
restaurant.number_served=10
print(restaurant.number_served)

'''setting new number through calling set_number_served method'''
restaurant.set_number_served(20)
print(restaurant.number_served)

'''setting new number through incrementing value method'''
restaurant.increment_number_served(10)
print(restaurant.number_served)





