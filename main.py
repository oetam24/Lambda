from dataclasses import dataclass, field

@dataclass
class Medal:
    dyscyplina: str
    typ: str

@dataclass
class Czlowiek:
    imie: str
    nazwisko: str
    wiek: int
    plec: str
    wzrost: int
    waga: int

@dataclass
class Sportowiec(Czlowiek):
    medale: list[Medal] = field(default_factory=list)

    def show_medale(self):
        zlote = list(filter(lambda x: x.typ == 'Złoty', self.medale))
        srebrne = list(filter(lambda x: x.typ == 'Srebrny', self.medale))
        brazowe = list(filter(lambda x: x.typ == 'Brązowy', self.medale))
        print(f'Złote: {len(zlote)}, Srebrne: {len(srebrne)}, Brązowe: {len(brazowe)}')

    def dodaj_medal(self, dyscyplina, typ):
        self.medale.append(Medal(dyscyplina, typ))

def show_titled_sportowcy(dyscyplina, lista_sportowcow):
    pass
    # sportowcy = list(filter(lambda x: medal.type for medal.in x.medale if medal.type == dyscyplina))

if __name__ == '__main__':
    sportowcy = []
    Adam = Sportowiec('Adam', 'Małysz', 40, 'M', 176, 49)
    Robert = Sportowiec('Robert', 'Lewandowski', 32, 'M', 180, 65)
    Anna = Sportowiec('Anna', 'Lewandowski', 30, 'K', 172, 55)
    sportowcy.append(Adam)
    sportowcy.append(Robert)
    sportowcy.append(Anna)
    Adam.dodaj_medal('Skoki narciarskie', 'Złoty')
    Adam.dodaj_medal('Skoki narciarskie', 'Złoty')
    Adam.dodaj_medal('Rajdy', 'Brązowy')
    Robert.dodaj_medal('Piłka nożna', 'Złoty')
    Robert.dodaj_medal('Piłka nożna', 'Srebrny')
    Robert.dodaj_medal('Nic', 'Złoty')
    Anna.dodaj_medal('Instagram', 'Złoty')
    Anna.dodaj_medal('Karate', 'Złoty')
    Anna.dodaj_medal('Karate', 'Srebrny')

    sportowcy = sorted(sportowcy, key=lambda x: x.wzrost, reverse=False)
    for sport in sportowcy:
        print(sport.imie, sport.nazwisko)

