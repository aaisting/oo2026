from abc import ABC, abstractmethod


class Auto(ABC): #liides
   @abstractmethod
   def kiirendab(self, amount: float) -> None:
       pass


   @abstractmethod
   def getSpeed(self) -> float:
       pass




class SimpleAuto(Auto): #realiseeriv klass
   def __init__(self):
       self.speed = 0
       self.acceleration_count = 0


   def kiirendab(self, amount: int) -> None:
       self.speed += amount
       self.acceleration_count += 1


   def getSpeed(self) -> int:
       return self.speed


   def getAccelerationCount(self) -> int:
       return self.acceleration_count


k = SimpleAuto()


k.kiirendab(50)
print("kiirus:", k.getSpeed())


k.kiirendab(40)
print("kiirus:", k.getSpeed())


k.kiirendab(30)
print("kiirus:", k.getSpeed())


k.kiirendab(20)
print("kiirus:", k.getSpeed())


k.kiirendab(10)
print("kiirus:", k.getSpeed())


print()


print("Lõplik kiirus:", k.getSpeed())
print("Kiirendusi kokku", k.getAccelerationCount())