class Vehil:
    name = "car"
    engine = 1
    cover = "housing"

    def set(self, name, engine, cover):
        self.name = name
        self.engine = engine
        self.cover = cover


class Motobyke(Vehil):
    corporation = "корпорація"
    weehls = 2

    def set1 (self, corporation, weehls):
        self.corporation = corporation
        self.weehls = weehls


yamaha = Motobyke()
yamaha.set("yamaha", 1.2, "moto")
yamaha.set1("yamaha", 2)
print(yamaha.name + " " + str(yamaha.engine)+ " " + yamaha.corporation + " " + str(yamaha.weehls) + " weehls")

dodge = Vehil()
dodge.set("Dodge", 2.5, "hachback")
print(dodge.name + " " + str(dodge.engine)+ " " + dodge.cover)

kia = Vehil()
kia.set("Kia", 1.6, "comby")
print(kia.name + " " + str(kia.engine)+ " " + kia.cover)


nokia = Vehil()
nokia.set("Dodge", 2.5, "hachback")
print(nokia.name + " " + str(nokia.engine)+ " " + nokia.cover)






