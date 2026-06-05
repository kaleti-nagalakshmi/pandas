class Car :
    name = "bmw"
    color = "red"
c1=Car()
print(c1.color)
print("\n")
      
class Student:
    def student_details(self,name,age):
        print(name,age)
c2=Student()
c2.student_details("naga",21)
print("\n")




class Cars:
    name = "bmw"
    color = "red"
    def speed(self):
        name2=self.name
        print(name2)
        print(self.color + self.name)
c3=Cars()
print(c3.name)
c3.speed()
print("\n")


# encapsulation 
class Student:
    def __init__(self):
        self.__marks = 90
    def sho(self):
        print(self.__marks)

obj=Student()
obj.marks=0
obj.sho()


class Bank1 :
    def __init__(self,balance):
        self.balance = balance
    def display(self):
        print(self.balance)
c4 = Bank1(200)
c4.display()
print("\n")


class Bank :
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

c5 = Bank()
c5.__balance=0
c5.deposit(500)
c5.withdraw(500)
c5.show_balance()
print("\n")

# inheritance
class grand_parent :
    def work(self):
        print("this is grandparent class")
        
        
class parent(grand_parent) :
    def test(self):
        
        print("this is parent class")
class child(parent):
    def display(self):
        print("this is child")
obj1=parent()
obj1.test()

obj2=child()
obj2.test()
obj2.display()
obj2.work()

# super() in inheritance

class employee:
    def work(self):
        self.e= 10
        self.d= 29
        print("employee working")
class developer(employee):
    def work(self):
        super().work()
        print("developer write a code")
        print(self.e + self.d)

class display(developer):
    def test(self):
        super().work()
    def work(self):
        print("test")

obj1 = developer()
obj1.work()


obj1 = display()
obj1.work()
obj1.test()
# calling parent method
class employee :
    def test(self,name):
        self.name = name
        
class developer(employee) :
    def work(self,name,roll):
        super().test(name)
        self.roll = roll
       
obj = developer()
obj.work("naga",24)
print(obj.roll,obj.name)




# super() with __init__ constructor
class naga :
    def __init__(self,name):
        self.name = name 
class student(naga):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll= roll
    
s = student("naga",25) 
print(s.name,s.roll)

# method overriding using super()
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        super().sound()
        print("dog barks")
a = dog()
a.sound()

# abstraction

from abc import ABC,abstractmethod
class ATM(ABC) :
    @abstractmethod
    def withdraw(self):
        pass
class SBI(ATM):
    def withdraw(self):
        print("withdraw from SBI ")
class HDFC(ATM):
    def withdraw(self):
        print("with from HDFC")
atm1= SBI()
atm1.withdraw()

atm2= HDFC()
atm2.withdraw()

from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("starting....")
c= car()
c.start()
        




        
        


    


