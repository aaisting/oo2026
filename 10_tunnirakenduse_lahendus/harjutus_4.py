#10 kg radiaator. 1 kraad soojenemist = 10 * 412 = 4120 J
# 1kw * 10 sek = 1000J. 10000/4120 ~ 2,43 kraadi
# 10 kraadi jahtumist - 41200 J
#41200 / 30 / 1245 = 1.1 kraadi toa õhk soojemaks
class Materjalikogus:
    def __init__(self, umass, uerisoojus,utemperatuur ):
        self.mass = umass
        self.uerisoojus = uerisoojus
        self.temperatuur = utemperatuur

    def kysiTemperatuur(self):
        return self.temperatuur

    def energiavahetus(self,j):
        self.temperatuur+= j/self.mass/self.uerisoojus

class ohukogus(Materjalikogus):
    def__init__(self, umass, uerisoojus, utemperatuur):
        super().__init__(pikkus*laius*korgus*1.23*1012, temperatuur)





radiaator = Materjalikogus(10, 412, 20)
print(radiaator.kysiTemperatuur())
print(radiaator.energiavahetus(1000))
print(radiaator.kysiTemperatuur())