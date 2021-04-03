class Szyfr:  # deklarujemy klase szyfr
    def __init__(self, tekst, krok):  # parametry to tekst do zaszyfrowania i krok do zaszyfrowania
        self.tekst = tekst
        self.krok = krok

    def szyfrowanie(self):  # metoda szyfrowanie
        zaszyfrowane = ""
        for i in range(len(self.tekst)):
            znak = self.tekst[i]
            if znak.isupper():  # jezeli jest to wielka litera alfabetu
                zaszyfrowane += chr((ord(znak) + self.krok - 65) % 26 + 65)  # dodajemy krok do kodu ascii
            else:  # jezeli mala litera alfabety                              #reszta z dzielenia 26 gdybysmy wyszli poza alfabet
                zaszyfrowane += chr((ord(znak) + self.krok - 97) % 26 + 97)
        return zaszyfrowane


def main():
    slowo = input("podaj tekst do zaszyfrowania (przyjumuje male i wielkie litery alfabetu angielskiego): ")
    krok = int(input("podaj krok o jaki zaszyfrowac tekst: "))
    wynik = Szyfr(slowo, krok)
    wynik = wynik.szyfrowanie()
    print(wynik)


if __name__ == "__main__":
    main()
