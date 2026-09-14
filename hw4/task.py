# Tarixlə bagli funksionallıq (bonus)
class TarixMixin:

    def elave_olundu(self):
        return f"{self.__class__.__name__} playlist-ə əlavə olundu"


class Mahni:

    def __init__(self, ad, ifaci, muddet):
        self.ad = ad
        self.ifaci = ifaci
        self.muddet = muddet

    def __str__(self):
        return f"{self.ad} - {self.ifaci} ({self.muddet} san)"

    def __repr__(self):
        return f"{self.ad}({self.muddet})"

    def __lt__(self, diger):
        return self.muddet < diger.muddet


class Podcast(Mahni):

    def __init__(self, ad, ifaci, muddet, bolum):
        super().__init__(ad, ifaci, muddet)
        self.bolum = bolum

    def __str__(self):
        return f"{super().__str__()} · bolum {self.bolum}"


class Playlist(TarixMixin):
    # __mro__ zənciri: Playlist -> TarixMixin -> object
    # Python metodu əvvəlcə Playlist sinfində axtarır, tapmasa TarixMixin-də,
    # oradan da tapmasa ən sonda object sinfində axtarır.

    def __init__(self):
        self.mahnilar = []

    def elave_et(self, mahni):
        self.mahnilar.append(mahni)

    def __contains__(self, ad):
        return any(mahni.ad == ad for mahni in self.mahnilar)

    def __len__(self):
        return len(self.mahnilar)

    def __add__(self, diger):
        yeni = Playlist()
        yeni.mahnilar = self.mahnilar + diger.mahnilar
        return yeni



    m = Mahni("Yellow", "Coldplay", 269)
    p = Podcast("Kosmos", "Elm saati", 1800, 12)
    print(m)
    print(p)

    mahnilar = [m, Mahni("Numb", "Linkin Park", 185)]
    print(sorted(mahnilar))

    pl1 = Playlist()
    pl2 = Playlist()
    pl1.elave_et(m)
    pl2.elave_et(p)
    print("Yellow" in pl1)

    birlesmis = pl1 + pl2
    print(len(birlesmis))
    print(len(pl1))

    print(pl1.elave_olundu())