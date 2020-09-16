class Restaurant():
    '''simple attempt to represent restaurant'''
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name#attribute
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print("The restaurant is called "+self.restaurant_name.title())
        print("Type of the restaurant is  "+self.cuisine_type.title())#'cuisine_type.title' only wont work,one must pass self in method and use it

    def open_restaurant(self):
        print("the restaurant "+self.restaurant_name+" is opened!!")


restaurant = Restaurant("Azo idea space", "Fine dinning")
print(restaurant.restaurant_name)#printing each attribute
print(restaurant.cuisine_type)
restaurant.describe_restaurant()#calling method from the class
restaurant.open_restaurant()