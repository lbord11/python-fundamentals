class Dog():
   """This docstring will discuss how to interact with our Dog class.

   Our Dog class will have two attributes - a name and happiness_level.
   It's one method, wag_tail, will simulate the dog wagging it's tail
   some number of times, and increasing it's happiness level.

   Parameters:
   -----------
       name: str
       happiness_level: int
   """

   def __init__(self, name, happiness_level=5):
       self.name = name
       self.happiness_level = happiness_level

   def wag_tail(self, n):
       """Wags the dogs tail n times, and each time increase
       happiness level by 5.

       Args:
           n: int
       """
       for i in range(n):
           self.happiness_level += 5


############


class Cat():
   """This docstring will discuss how to interact with our Cat class.

   Our Cat class will have three attributes - a name, laziness level,
   and a location. It's one method, sense_earthquake, will change
   the cats location based on whether or not there is an earthquake.

   Parameters
   ----------
       name: str
       laziness_level: int
           This holds how lazy the cat is on a scale of 1 to 10.
       location: str
           This holds where the cat is currently located at.
   """

   def __init__(self, name, laziness_level = 5, location = "home"):
       self.name = name
       self.laziness_level = laziness_level
       self.location = location

   def sense_earthquake(self, earthquake):
       """Checks if the cat senses an earthquake, and if so changes the cat's
       location to 'gone dark'.

       Args:
           earthquake: boolean
               Holds a True or False as to whether there was an earthquake.
       """
       if earthquake:
           self.location = "gone dark"


############
#Part 2

class Car():

    def __init__(self, model, color, tank_size):
        self.model = model
        self.color = color
        self.tank_size = tank_size
        self.gallons_of_gas = self.tank_size # We're assuming its tank is full.

    def drive(self, miles_driven):
        self.gallons_of_gas -= miles_driven / 10.

#######


class Plane():

    def __init__(self, destination, departure_city, trip_distance):
        self.destination = destination
        self.departure_city = departure_city
        self.trip_distance = trip_distance

    def fly(self):
        self.departure_city, self.destination = self.destination, self.departure_city

#Assignment Qs
##############



class Company():

    def __init__(self,name,industry_type,num_employees,total_revenue):
        self.name = name
        self.industry_type = industry_type
        self.num_employees = num_employees
        self.total_revenue = total_revenue

    def serve_customer(self,serving_customer_cost):
        self.total_revenue -= serving_customer_cost

    def gain_employees(self,list_of_new_emp):
        self.num_employees += len(list_of_new_emp)


#######

class TV():

    def __init__(self, brand, on_status = False, current_channel = 0, life_perc = 100):
        self.brand = brand
        self.on_status = on_status
        if self.on_status == False:
            self.current_channel = 0
        else:
            self.current_channel = current_channel
        self.life_perc = life_perc

    def hit_power(self):
        if self.on_status == True:
            self.on_status = False
            self.life_perc -= 0.01
            self.current_channel = 0
        elif self.on_status == False:
            self.on_status = True
            self.current_channel = 1

    def change_channel(self, num):
        if self.on_status == True:
                self.current_channel = num
        else:
            print ("Television Not On!")
