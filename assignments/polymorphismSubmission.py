
# Parent class vehicle
class Vehicle:
      year = "2011"
      make = "subaru"
      model = "legacy"
      engine_type = "four cylinder"

      def buyVehicleInfo(self):
            entry_year = input("Enter vehicle year: ")
            entry_make = input("Enter vehicle make: ")
            entry_model = input("Enter vehicle model: ")
            engine_type = input("Enter vehicle engine: ")
                  print("Sweet! We'll find a {} {} {} with a {} engine for your as soon as we can!".format(entry_year,entry_make,entry_model,engine_type))
            


# Child class plane
class Plane(Vehicle):
      number_of_wings = 2
      licence_requirement = "Commercial Pilot's Licence"
      turbine_type = "underwing turbofan"

      def buyVehicleInfo(self):
              entry_year = input("Enter vehicle year: ")
            entry_make = input("Enter vehicle make: ")
            entry_model = input("Enter vehicle model: ")
            turbine_type = input("Enter vehicle engine: ")
                  print("Sweet! We'll find a {} {} {} with {} turbines for your as soon as we can!".format(entry_year,entry_make,entry_model,turbine_type))
            

            

# Child class boat
class Boat(Vehicle):
      boat_type = "commercial fishing"
      water_type = "ocean"
      motor_type = "marine diesel"

      def buyVehicleInfo(self):
              entry_year = input("Enter vehicle year: ")
            entry_make = input("Enter vehicle make: ")
            entry_model = input("Enter vehicle model: ")
            motor_type = input("Enter vehicle engine: ")
                  print("Sweet! We'll find a {} {} {} with a {} motor for your as soon as we can!".format(entry_year,entry_make,entry_model,motor_type))
            

      

      
    
