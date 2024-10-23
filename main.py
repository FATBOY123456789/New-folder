from abc import ABC,abstractmethod
class ABCLASS(ABC):
    def show(self,x):
        print('value is: ',x)
    @abstractmethod
    def display(self):
        print('hi in abstract :( ')
class A1(ABCLASS):
    def display(self):
        print('hi in NOT abstract :) ')
ob1=A1()
ob1.show(69420)
ob1.display()