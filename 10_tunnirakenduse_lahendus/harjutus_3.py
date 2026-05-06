#Koosta või otsi eestpoolt soojendatava veekoguse klass.

#Arvesta, et kann mahutab kuni kaks liitrit. Täis kann jahtub 100 kraadi pealt 20-kraadise välistemperatuuri juures 100 sekundi jooksul ühe kraadi. Arvuta, mitu džauli energiat iga erinevuskraadi kohta 100 sekundi jooksul üle kandub.

#Lisa klassile käsklus 100 sekundi jagu jahtumiseks. Tühjema kannu puhul eraldub soojusenergia sama kiiresti, kann aga jahtub rutem. Näiteks ühe liitri vee puhul saja kraadi juures kaks kraadi, poole liitri vee puhul neli kraadi.

#Veendu, et käsk töötab õigesti ka väiksema temperatuuride vahe korral. Näiteks 30-kraadise toatemperatuuri puhul peaks poole liitri veega kann jahtuma 100 sekundi jooksul kaks kraadi.

#Lisa käsklus kannu jahtumise simuleerimiseks 100 sekundi kaupa. Iga etapi juures arvutatakse jahtumiskiirus uuesti. Leia nõnda kannu temperatuur 1000 sekundi möödudes. Kuva temperatuur iga etapi järel.


#kui palju väheneb vahe 3600 sekundi jooksul

#alguses vahe 100%
#30 sek vahe 99%
#60 sek vahe 99%
#90 sek vahe 98.01%
class VeeSoojendamine:
    def __init__(self, valis_temp, kannu_temp, maht_liitrites):
        self.valis_temp = valis_temp
        self.kannu_temp = kannu_temp
        self.maht = maht_liitrites
        self.max_maht = 2.0
        self.energia_1kraadi_100sek = self.c * self.rho * self.max_maht * 1  # J


    def jahutus_100sek(self):
        suvaline_muutuja = self.kannu_temp - self.valis_temp
        if suvaline_muutuja <= 0:
            return 0
        kraadilangus = suvaline_muutuja * (self.max_maht / self.maht)
        self.kannu_temp -= kraadilangus
        return kraadilangus

    def simuleeri(self, aeg_s, samm=100):
        for i in range(samm):
            self.jahutus_100sek()
