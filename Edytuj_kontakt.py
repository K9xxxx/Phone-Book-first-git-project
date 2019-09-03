import Dodaj_kontakt
i=0
arr_im=[]       #Lista imion
arr_naz=[]      #Lista nazwisk
arr_nr_tele=[]  #Lista Numerow telefonow
tab_le=[]       #Lista z iloscia lini
tab_new=[]      #Lista z kontaktami
tab_new2=[]     #Lista z kontaktami
suma=0

r=open("Ksiazka Telefoniczna",mode="a+")
r.seek(0)

"""Przelicza ilosc lini w pliku txt"""
with open("Ksiazka Telefoniczna") as f:
    for i,l in enumerate(f):
        pass            # Pusta komenda stosowana gdy jest wymagana jakas komenda jak np. tutaj w funkcji
    ilosc_lini=i
i=int(0)

while i<=ilosc_lini:
    tab_le.append(len(r.readline())) #Zlicza ilosc znakow z pojedynczej linijki oraz ta wartosc dodaje do listy
    i=i+1

i=int(0)
r.seek(0)

"""Pentla usuwajaca znak '\n' oraz dodajaca wyrazy z poszczegolnej lini do listy"""
while i<=ilosc_lini:
    if i==ilosc_lini:
        odczyt=r.read(tab_le[i])
    else:
        odczyt=r.read(tab_le[i]-1)
    tab_new.append(odczyt) #dodaje wyraz bez \n do listy
    suma=suma+tab_le[i]
    seek=r.seek(suma+i+1)
    i=i+1
a=0
b=1
c=2

"""Bloki przypisujace odpowiednio numer, imie i nazwisko do odpowiednich list"""
while a<=len(tab_le):
    try:
        arr_nr_tele.append(tab_new[a])
        a=a+3
    except IndexError:
        break
while b<=len(tab_le):
    try:
        arr_im.append(tab_new[b])
        b=b+3
    except IndexError:
        break
while c<=len(tab_le):
    try:
        arr_naz.append(tab_new[c])
        c=c+3
    except IndexError:
        break

i=0

while i+1<=len(arr_nr_tele):
    try:
        print(str(i+1)+". "+arr_im[i]+" "+arr_naz[i]+" ( "+arr_nr_tele[i]+" )")
    except IndexError:
        break
    i=i+1
print("Ktory kontakt chcesz edytowac?: ", end='')
choose=int(input(""))

"""Usuwanie pozycji na listach"""
arr_nr_tele.remove(arr_nr_tele[choose-1])
arr_im.remove(arr_im[choose-1])
arr_naz.remove(arr_naz[choose-1])

tab_new.remove(tab_new[choose*3-1])
tab_new.remove(tab_new[choose*3-2])
tab_new.remove(tab_new[choose*3-3])

print("Wprowadz ponownie kontakt")
_nr_tele=Dodaj_kontakt.dodaj_nr_tel()
_imie=Dodaj_kontakt.dodaj_imie()
_nazwisko=Dodaj_kontakt.dodaj_nazwisko()

"""Wprowadza nowa pozycje na miejsce wczesniejszej zmienianej"""
arr_nr_tele.insert(choose-1,_nr_tele)
arr_im.insert(choose-1,_imie)
arr_naz.insert(choose-1,_nazwisko)

tab_new.insert(choose*3-3,arr_nr_tele[choose-1])
tab_new.insert(choose*3-2,arr_im[choose-1])
tab_new.insert(choose*3-1,arr_naz[choose-1])

"""Blok kodu odpowiadajacy za usuwanie listy by nastepnie ponownie ja wypisac w pliku"""
with open("Ksiazka Telefoniczna","r") as f:
    lines=f.readlines()
with open ("Ksiazka Telefoniczna","w") as f:
    for line in lines:
        del line
"""test"""
"""test2"""

r.close()
