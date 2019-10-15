#zad1
tekst = 'Do czego tego użyć? Ogólnie znana teza głosi, iż użytkownika może rozpraszać zrozumiała zawartość strony, kiedy ten chce zobaczyć sam jej wygląd. Jedną z mocnych stron używania Lorem Ipsum jest to, że ma wiele różnych „kombinacji” zdań, słów i akapitów, w przeciwieństwie do zwykłego: „tekst, tekst, tekst”, sprawiającego, że wygląda to „zbyt czytelnie” po polsku. Wielu webmasterów i designerów używa Lorem Ipsum jako domyślnego modelu tekstu i wpisanie w internetowej wyszukiwarce ‘lorem ipsum’ spowoduje znalezienie bardzo wielu stron, które wciąż są w budowie. Wiele wersji tekstu ewoluowało i zmieniało się przez lata, czasem przez przypadek, czasem specjalnie (humorystyczne wstawki itd).'
imie='Marta'
nazwisko='Rozmyslowicz'

class Osoba:

#zad2
    def __init__(self, imie, nazwisko, tekst):
        #zad1
        self.tekst=tekst
        #Zad2
        self.imie=imie
        self.nazwisko=nazwisko

    def ileLiter(self):
        litera1 = self.imie[2]
        litera2 = self.nazwisko[3]
        ile1 = self.tekst.count(litera1)
        ile2 = self.tekst.count(litera2)
        print(f'Pierwsza litera ' +litera1 + ' Druga litera ' + litera2)
        print(f'pierwsza litera ' +litera1 + ' powtorzyla sie ' + ' %i' %ile1)
        print(f'pierwsza litera ' + litera2 + ' powtorzyla sie ' + ' %i' %ile2)
#zad 5 bez kapitalikow
    def odwroc(self):
        imie1=imie[::-1]
        nazwisko1=nazwisko[::-1]
        print(f'odwrocone imie: '+ imie1 + ' ' +nazwisko1)

#zad6
    def podzielListe(self):
        lista=[]
        lista2=[]
        #wypelnienie listy pierwszej
        for i in range(1,11):
            lista.append(i)
        print(lista)
        #dodtanie polowy listy do lista2
        for j in range(5, 10):
            lista2.append(lista[j])

        sObject=slice(0,5,1)
        lista1=lista[sObject]
        #for k in range(5, 9):
         #   lista.remove(lista[k])
        print(lista1)
        print(lista2)
        #zad7
        lista3=lista1 +lista2
        print(lista3)













#wywolanie zad2
test=Osoba(imie, nazwisko, tekst)
test.ileLiter()
# zad5
test.odwroc()
#zad 6, 7
test.podzielListe()






