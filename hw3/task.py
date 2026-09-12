class Film:

    def __init__(self, ad, il, reyting):
        self.ad = ad
        self.il = il
        self.reyting = reyting 

    @property
    def ad(self):
        return self._ad

    @ad.setter
    def ad(self, deyer):
        self._ad = deyer

    @property
    def il(self):
        return self._il

    @il.setter
    def il(self, deyer):
        self._il = deyer

    @property
    def reyting(self):
        return self._reyting

    @reyting.setter
    def reyting(self, deyer):
        if deyer < 0 or deyer > 10:
            raise ValueError("Reyting 0-10 aralığında olmalıdır")
        self._reyting = deyer

    @classmethod
    def from_string(cls, text):
        ad, il, reyting = text.split("|")
        return cls(ad, int(il), float(reyting))

    def __str__(self):
        return f"{self.ad} ({self.il}) - reyting {self.reyting}"

    def __eq__(self, diger):
        return self.ad == diger.ad and self.il == diger.il

    def __hash__(self):
        return hash((self.ad, self.il))


class FilmSiyahisi:

    def __init__(self):
        self.filmler = []
    def elave_et(self, film):
        self.filmler.append(film)

    def __len__(self):
        return len(self.filmler)

    def en_yaxsi(self):
        return max(self.filmler, key=lambda film: film.reyting)



f = Film("Inception", 2010, 8.8)
print(f)
try:
    f.reyting = 12
except ValueError as e:
    print(e)

f2 = Film.from_string("Interstellar|2014|8.6")
print(f2)

s = FilmSiyahisi()
s.elave_et(Film.from_string("Inception|2010|8.8"))
s.elave_et(Film.from_string("Interstellar|2014|8.6"))
print(len(s))
print(s.en_yaxsi())