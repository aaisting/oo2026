import math
valis_temp = float(input("Sisesta välistemperatuur: "))
kannu_temp = float(input("Sisesta kannu temperatuur: "))
jahtus_30s = float(input("Kui palju jahtus 30 sekundiga: "))

temp_vahe = kannu_temp - valis_temp
kordaja = jahtus_30s / temp_vahe

uus_temp = float(input("Sisesta temperatuur, mille juures tahad jahtumist teada: "))

uus_vahe = uus_temp - valis_temp
uus_jahtumine = kordaja * uus_vahe

print(" etteantud temperatuuril jahtutud kraadide arv 30 sekundi jooksul:",uus_jahtumine)
