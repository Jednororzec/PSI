import file_manager as a

def zad2(data_text):
    x=len(data_text)
    #y=data_text[0:x]
    def y (data_text,x):
        for i in range(x):
            print(data_text[i])
    slownik = dict(length=x,letters=y(data_text,x), big_letters=data_text.upper(), small_letters=data_text.lower())
    print(slownik.values())



def temp (celcjusz):    #zad4
    if celcjusz>=-274:
        Kelvin=celcjusz-274
        Fahrenheit=9/7*celcjusz +32    #T[oF] = 32 + 9/5 T[oC]
        Rankine=Fahrenheit +459
        print(f'w Celcjuszach %i Kelvinach %i Farenhaitach %i Rankinach %i' %(celcjusz,Kelvin,Fahrenheit,Rankine ))




#data_text = input('Podaj liczbę całkowitą: ')
#data_text = str(data_text)
#celcjusz=input('Podaj temp w celcjuszach')
#celcjusz =int(celcjusz)


#zad2(data_text)
#temp(celcjusz)

file=FileManager('plik.txt')
dane=file.read_file()
file.update_file(dane)
file.read_file()