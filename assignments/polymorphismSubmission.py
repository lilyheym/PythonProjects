
# Parent class vehicle
class Vehicle:
      year = "2011"
      make = "subaru"
      model = "legacy"
      transport_type = "land"

      def buyVehicleInfo(self):
            entry_year = input("Enter vehicle year: ")
            entry_make = input("Enter vehicle make: ")
            entry_model = input("Enter vehicle model: ")
                  print("Sweet! We'll findd a {} {} {} for your as soon as we can!".format(entry_year,entry_make,entry_model))
            


# Child class plane
class Plane:
      number_of_wings = 2
      licence_requirement = "Commercial Pilot's Licence"
      transport_type = "air"

# Child class boat
class Boat:
      boat_type = "commercial fishing"
      water_type = "ocean"
      transport_type = "water"
      
      
      
      
    