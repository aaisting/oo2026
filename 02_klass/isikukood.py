class Isikukood:
  def __init__(self, isikukood):
   if len(isikukood)!=11: 
     raise Exception("Vigane pikkus")
   numbrid=[int(nr) for nr in isikukood]
   koefd=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
   if sum([paar[0]*paar[1] for paar in zip(numbrid, koefd)]) % 11!=int(isikukood[-1]):
       raise Exception("Esimesel ringil kood ei sobi")
   self.kood=isikukood
  def kuupaev(self):
      return self.kood[5:7]
  #koosta funktsioon, mis annab kuu nime sõnana
  def kuunimi(self):
      kuud=["", "jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
      return kuud[int(self.kood[3:5])]
  #Koosta funktsioon neljakohalise sünniaasta jaoks
  def aasta(self):
      nr=int(self.kood[0])
      return int(nr/2)*100+1800+int(self.kood[1:3])
        
ik1=Isikukood("37605030299")
print(ik1.kuupaev())
print(ik1.kuunimi())
print(ik1.aasta())