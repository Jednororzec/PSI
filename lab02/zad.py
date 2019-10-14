tekst = 'Do czego tego użyć? Ogólnie znana teza głosi, iż użytkownika może rozpraszać zrozumiała zawartość strony, kiedy ten chce zobaczyć sam jej wygląd. Jedną z mocnych stron używania Lorem Ipsum jest to, że ma wiele różnych „kombinacji” zdań, słów i akapitów, w przeciwieństwie do zwykłego: „tekst, tekst, tekst”, sprawiającego, że wygląda to „zbyt czytelnie” po polsku. Wielu webmasterów i designerów używa Lorem Ipsum jako domyślnego modelu tekstu i wpisanie w internetowej wyszukiwarce ‘lorem ipsum’ spowoduje znalezienie bardzo wielu stron, które wciąż są w budowie. Wiele wersji tekstu ewoluowało i zmieniało się przez lata, czasem przez przypadek, czasem specjalnie (humorystyczne wstawki itd).'


class lab02:

    def __init__(self, imie, nazwisko, tekst):
        #zad1
        self.tekst=tekst
        #Zad2
        self.imie=imie
        self.nazwisko=nazwisko

    def ileLiter(self):
        litera1=self.imie[2]
        litera2=self.nazwisko[3]
        ile1=self.tekst.count(litera1)
        ile2 = self.tekst.count(litera2)
        print (f'Pierwsza litera ' +litera1 + ' Druga litera ' + litera2 )
        print(f'pierwsza litera ' +litera1 + ' powtorzyla sie ' + ' %i' %ile1)
        print(f'pierwsza litera ' + litera2 + ' powtorzyla sie ' + ' %i' % ile2)

test=lab02('Marta', 'Rozmyslowicz', tekst)
test.ileLiter()


