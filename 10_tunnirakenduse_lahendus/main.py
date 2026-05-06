import math
class Takisti:


   def __init__(self, takistus, nimi=""):
       self.takistus = takistus  #R(oomid)
       self.nimi = nimi


   def ütle_takistus(self):
       return self.takistus  # R = takistus(oomid)


   def arvuta_voolu_tugevus(self, pinge): # I(Amprid) = U(voldid) / R(takistus)  (Amprid)
       return pinge / self.takistus


   def arvuta_pinge(self, voolu_tugevus):# U(Voldid) = I(vooolutugevus) * R(takistus)
       return voolu_tugevus * self.takistus


   def arvuta_võimsus(self, pinge):
       return pinge * self.arvuta_voolu_tugevus(pinge)  # P(vattid) = U(voldid) * I(voolu_tugevus)


#-----------------------------------------------------------------------------------------------------------------------
class Rööp_ühendus:
   def __init__(self, nimi="Rööp"):
       self.nimi = nimi
       self.elemendid = []


   def lisa(self, element):
       self.elemendid.append(element)


   def ütle_takistus(self):
       suvaline_muutuja = 0
       for i in self.elemendid:
           suvaline_muutuja += 1 / i.ütle_takistus()
       return 1 / suvaline_muutuja


   def arvuta_koguvoolu_tugevus(self, pinge):
       koguvool = 0
       for i in self.elemendid:
           koguvool += i.arvuta_voolu_tugevus(pinge)
       return koguvool




#-----------------------------------------------------------------------------------------------------------------------
# Takistite näide


print("-------------------takisti-------------------")
print("Loo programmiga kolm takistit. Esimese takistus 110 oomi, teise takistus 220 oomi, kolmanda takistus 4700 oomi (ehk 4,7 kilooomi). Arvuta iga takisti puhul voolu_tugevus 5-voldise pinge korral.")
print()


t1 = Takisti(110)
t2 = Takisti(220)
t3 = Takisti(4700)


pinge = 5#Volti


voolu_tugevus_t1 = t1.arvuta_voolu_tugevus(pinge)
voolu_tugevus_t2 = t2.arvuta_voolu_tugevus(pinge)
voolu_tugevus_t3 = t3.arvuta_voolu_tugevus(pinge)


print("T1 voolu_tugevus =", voolu_tugevus_t1)
print("T2 voolu_tugevus =", voolu_tugevus_t2)
print("T3 voolu_tugevus =", voolu_tugevus_t3)
print()


#-----------------------------------------------------------------------------------------------------------------------
print("-------------------harjutus(füüsika)-------------------")
print("Takistile mõjub pinge 5 volti ning seda läbib vool 2 amprit. Mitu vatti soojust eraldub takistist?")
print("Takistile mõjub pinge 4 volti ning sealt eraldub võimsus 6 vatti. Mitu amprit voolu läbib takistit?")
print("Mitu oomi on eelneva takisti takistus?")
print("Veekeedukannu  võimsuseks on 1 kilovatt, seal sees on vett 1 liiter. Mitme kraadi peale tõuseb vee temperatuur 20 kraadi Celsiuse pealt ühe minutiga, kui kogu sisselülitatud kannu võimsus läheb vee soojendamiseks?")
print("Mitu amprit voolu läbib eelnimetatud veekeedukannu, kui võrgupinge on 220 volti?")
print("Mitu oomi on selle veekeedukannu takistus?")


print("Võimsus (P=U*I):", 5 * 2)
print("voolu_tugevusu tugevus (I=U/R):", 6 / 4)
print("Takistus (R=U/I):", 4 / (6 / 4))


energia = 1000 * 60
temperatuuri_tous = energia / 4190
print("Temperatuuri tõus (ΔT = Q/mc):", temperatuuri_tous)


voolu_tugevus = 1000 / 220
takistus = 220 / voolu_tugevus
print("voolu_tugevusu tugevus (I=U/R):", voolu_tugevus)
print("Takistus (R=U/I):", takistus)
print()


#-----------------------------------------------------------------------------------------------------------------------
print("-------------------harjutus(füüsika)-------------------")
print("Jalgratta tulede patarei pinge on 4,5 volti. Esituld läbiv vool 1 amper. Milline on esitule võimsus? Milline on esitule takistus?")
print("Sama jalgratta tagatuld läbib vool 0,5 amprit. Milline on tagatule võimsus? Milline on tagatule takistus?")
print("Milline on kahest rööbiti ühendatud jalgrattatulest koosneva lampide süsteemi võimsus kokku 4,5 voldi juures? Milline on selle lampide süsteemi kogutakistus oomides?")


pinge = 4.5  # Volt


# Esituli
esituli_vool = 1  # Amprid
esituli = Takisti(pinge / esituli_vool, "Esituli")  # R = U / I
esituli_võimsus = esituli.arvuta_võimsus(pinge)
# Tagatuli
tagatuli_vool = 0.5  # Amprid
tagatuli = Takisti(pinge / tagatuli_vool, "Tagatuli")  # R = U / I
tagatuli_võimsus = tagatuli.arvuta_võimsus(pinge)
print("Esituli vool:", esituli_vool, "A")
print("Esituli takistus:", esituli.ütle_takistus(), "oomi")
print("Esituli võimsus:", esituli_võimsus, "W")
print()
print("Tagatuli vool:", tagatuli_vool, "A")
print("Tagatuli takistus:", tagatuli.ütle_takistus(), "oomi")
print("Tagatuli võimsus:", tagatuli_võimsus, "W")
print()


rööp = Rööp_ühendus()
rööp.lisa(esituli)
rööp.lisa(tagatuli)


koguvool = rööp.arvuta_koguvoolu_tugevus(pinge)
koguvõimsus = pinge * koguvool
kogutakistus = rööp.ütle_takistus()


print("Rööbiti ühendatud tulest koosneva süsteemi koguvool:", koguvool, "A")
print("Rööbiti ühendatud tulest koosneva süsteemi koguvõimsus:", koguvõimsus, "W")
print("Rööbiti ühendatud tulest koosneva süsteemi kogutakistus:", kogutakistus, "oomi")

