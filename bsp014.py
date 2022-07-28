#Der Kunde geht in den Laden und kauft ein Laib Brot


class Kunde:
    vorname = None
    nachname = None
    geldboerse = 0
    tasche = []
    ort = None

    def __init__(self):
        self.vorname = "Max"
        self.nachname = "Mustermann"

    def kaufen(self, gegenstand):
        if self.geldboerse >= gegenstand.preis:
            self.tasche.append(gegenstand)
            self.geldboerse -= gegenstand.preis
        
    def gehen(self, ort):
        if ort.isOffen:
            self.ort = ort
            return
        return



class Laden:
    isOffen = None
    anzahlKunden = 0

    def __init__(self):
        self.isOffen = True


class Brot:
    sorte = None
    preis = 0

    def __init__(self):
        self.preis = 3
        self.sorte = "Korbbrot"

    
k = Kunde()
#k.vorname = "Max"
#k.nachname = "Mustermann"

l = Laden()
#l.isOffen = True

b = Brot()
#b.preis = 2.50
#b.sorte = "Gerster"

k.geldboerse += 5

k.gehen(l)
k.kaufen(b)

print(k.geldboerse,k.tasche,k.ort)









