class Fruit:     #class
      def __init__ (self):
            self._protected = 'protected'   #protected variable
            self.__private = 'private'    #private variable
            
      def meth(self):  #method to print
            print(self._protected)
            print(self.__private)



fruit = Fruit()
fruit.meth()
print(fruit)
