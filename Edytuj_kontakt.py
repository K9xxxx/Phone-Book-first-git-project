import Dodaj_kontakt
"""
Dzialanie programu:
Program przelicza ilosc lini z pliku txt nastepnie dodaje wartosci tych lini do tablicy ogolnej(tab_new)
Nastepnie sortuje wartosci z listy tab_new na poszczeglne wyznaczone do odpowiedniej 
informacji(arr_nr_tele,arr_im,arr_naz)
Nastepnie wyswietla informacje z tych list dla uzytkownika
jezeli uzytkownik wprowadzi zmiany to dane ktore zmienial sa zastepowane tymi nowymi na tych samych pozycjach w listach
Nastpenie usuwana jest cala zawartosc pliku txt oraz ponowne wpisanie wartosci z tablic do pliku
"""

i = 0
arr_num_alarm=("997","Policja"," ","998","Straz Pozarna"," ","999","Pogotowie"," ")
arr_im = []  # Lista imion
arr_naz = []  # Lista nazwisk
arr_nr_tele = []  # Lista Numerow telefonow
tab_le = []  # Lista z iloscia lini
tab_new = []  # Lista z kontaktami

def dodanie_stalych_do_listy():
    with open("Ksiazka Telefoniczna",mode='a+') as w:
        if ilosc_lini()==0 or ilosc_lini()==False:
            k=0
            while k <= len(arr_num_alarm):
                if k != 8:
                    w.write(arr_num_alarm[k] + '\n')
                else:
                    w.write(arr_num_alarm[k])
                    break
                k = k + 1
            print('y')
        else:
            print('x')
            pass
        w.seek(0)

def ilosc_lini():
    i=0
    """Przelicza ilosc lini w pliku txt"""
    with open("Ksiazka Telefoniczna",mode='r') as f:
        for i,l in enumerate(f):
            pass            # Pusta komenda stosowana gdy jest wymagana jakas komenda jak np. tutaj w funkcji
        ilosc_lini=i
    return ilosc_lini

def dodanie_do_listy(linie):
    suma = 0
    r=open("Ksiazka Telefoniczna",mode="a+")
    r.seek(0)
    i=int(0)
    while i<=linie:
        tab_le.append(len(r.readline())) #Zlicza ilosc znakow z pojedynczej linijki oraz dodaje ta wartosc do listy
        i=i+1

    i=int(0)
    r.seek(0)

    """Pentla usuwajaca znak '\n' oraz dodajaca wyrazy z poszczegolnej lini do listy"""
    while i<=linie:
        if i==linie:
            odczyt=r.read(tab_le[i])
        else:
            odczyt=r.read(tab_le[i]-1)
        tab_new.append(odczyt) #dodaje wyraz bez \n do listy
        suma=suma+tab_le[i]
        r.seek(suma+i+1)
        i=i+1

    r.close()

def sortowanie_do_list():
    dodanie_do_listy(ilosc_lini())
    """Bloki przypisujace odpowiednio numer, imie i nazwisko do odpowiednich list"""
    a = 0
    b = 1
    c = 2
    while a <= len(tab_le):
        try:
            arr_nr_tele.append(tab_new[a])
            a = a + 3
        except IndexError:
            break
    while b <= len(tab_le):
        try:
            arr_im.append(tab_new[b])
            b = b + 3
        except IndexError:
            break
    while c <= len(tab_le):
        try:
            arr_naz.append(tab_new[c])
            c = c + 3
        except IndexError:
            break
    print(tab_new)

def pout_listy_kontaktow():
    """ wyswietla kontakty w programie """

    sortowanie_do_list()

    i=int(0)
    while i+1<=len(arr_nr_tele):
        try:
            print(str(i+1)+". "+arr_im[i]+" "+arr_naz[i]+" ( "+arr_nr_tele[i]+" )")
        except IndexError:
            break
        i=i+1

def usuwanie_listy():
    """Blok kodu odpowiadajacy za usuwanie listy ( by nastepnie ponownie ja wypisac w pliku )"""
    with open ("Ksiazka Telefoniczna","r+") as f:
        f.seek(0)
        for index_of_line,line in enumerate(f):
            if index_of_line>8:
                del line

def usuwanie_pozycji(ktory_kontakt):
    """Usuwanie okreslonej pozycji w listach"""
    arr_nr_tele.remove(arr_nr_tele[ktory_kontakt - 1])
    arr_im.remove(arr_im[ktory_kontakt - 1])
    arr_naz.remove(arr_naz[ktory_kontakt - 1])

    tab_new.remove(tab_new[ktory_kontakt * 3 - 1])
    tab_new.remove(tab_new[ktory_kontakt * 3 - 2])
    tab_new.remove(tab_new[ktory_kontakt * 3 - 3])

def ponowne_dodanie_z_listy_do_pliku():
    """Wprowadzenie informacji z listy(tab_new) do pliku """
    with open("Ksiazka Telefoniczna", 'w') as f:
        for number_of_index, index in enumerate(tab_new):
            if number_of_index!=0:
                f.write("\n")
            f.write("{}".format(index))

def usuwanie_kontaktu():
    pout_listy_kontaktow()
    print("\nKtory kontakt chcesz usunac: ",end='')
    wybor_osoby=int(input())
    usuwanie_pozycji(wybor_osoby)
    ponowne_dodanie_z_listy_do_pliku()

def edytuj_kontakt_main():
    r=open("Ksiazka Telefoniczna", mode="a+")
    dodanie_stalych_do_listy()
    pout_listy_kontaktow()

    print("\nKtory kontakt chcesz edytowac?: ", end='')
    choose=int(input(""))

    usuwanie_pozycji(choose)

    print("Wprowadz ponownie kontakt")
    """Wprowadza nowa pozycje na miejsce wczesniejszej ktora zostala poddana zmianie"""
    arr_nr_tele.insert(choose-1,Dodaj_kontakt.dodaj_nr_tel())
    arr_im.insert(choose-1,Dodaj_kontakt.dodaj_imie())
    arr_naz.insert(choose-1,Dodaj_kontakt.dodaj_nazwisko())

    tab_new.insert(choose*3-3,arr_nr_tele[choose-1])
    tab_new.insert(choose*3-2,arr_im[choose-1])
    tab_new.insert(choose*3-1,arr_naz[choose-1])

    usuwanie_listy()

    ponowne_dodanie_z_listy_do_pliku()
    r.close()
