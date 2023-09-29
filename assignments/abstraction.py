from abc import ABC, abstractmethod   # import

class dinner(ABC):   # parent

      def dinnerBill(self, amount):
            print("The meal total is: ", amount)

      @abstractmethod  # defines the method as abstract
      def payment(self, amount):
            pass

class CashPayment(dinner):  # child class

      def payment(self, amount):
            print("Standard tip will be 15% of {}".format(amount))

# object

obj = CashPayment()
obj.dinnerBill("$63")
obj.payment("$63")
