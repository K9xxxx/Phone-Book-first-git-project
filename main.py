import Dodaj_kontakt

print("Ksiazka Telefoniczna")
print("Wybierz numer z mozliwych ponizej:")
print("1.Dodaj kontakt")
print("2.Edytuj kontakt")
print("3.Usun kontakt")
x=input("Co wybierasz: ")
f=open("Ksiazka Telefoniczna","a+")
if x=='1':
    nr_tele = Dodaj_kontakt.dodaj_nr_tel()
    f.write("\n"+nr_tele+"\n")

    imie=Dodaj_kontakt.dodaj_imie()
    f.write(imie+"\n")

    nazwisko=Dodaj_kontakt.dodaj_nazwisko()
    f.write(nazwisko)

elif x=='2':
    pass

f.close()