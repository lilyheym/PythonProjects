from abc import ABC, abstractmethod

class dinner(ABC):

      def dinnerBill(self, amount):
            print("The meal total is: ", amount)

      @abstractmethod
      def payment(self, amount):
            pass

class CashPayment(dinner):

      def payment(self, amount):
            print("Standard tip will be 15% of {}".format(amount))

obj = CashPayment()
obj.dinnerBill("$63")
obj.payment("$63")
