class Reszta:

    def wczytywanie_kwoty(self):

        kwota = input('Reszta do wydania: \nwpisz np. 2.56 lub 2.0').split('.')
        x = int(kwota[0])
        y = int(kwota[1])
        self.x = x
        self.y = y

    def wydawanie(self):
        zl = [500, 200, 100, 50, 20, 10, 5, 2, 1]
        gr = [50, 20, 10, 5, 2, 1]

        reszta_zl = [0] * len(zl)
        reszta_gr = [0] * len(gr)
        a = self.x
        b = self.y

        w1 = a
        w2 = b
        for id, c in enumerate(zl):
            reszta_zl[id], w1 = divmod(w1, c)

        for id, c in enumerate(gr):
            reszta_gr[id], w2 = divmod(w2, c)

        for kwota, c in zip(reszta_zl, zl):
            if c > 5 and kwota:
                print(kwota, "banknot/y", "->", c, "zl")
            elif kwota:
                print(kwota, "banknot/ty", "->", c, "zl")

        for kwota, c in zip(reszta_gr, gr):
            if kwota:
                print(kwota, "monata/ty", "->", c, "gr")


def main():
    kwota = Reszta()
    kwota.wczytywanie_kwoty()
    kwota.wydawanie()

if __name__ == "__main__":
    main()
