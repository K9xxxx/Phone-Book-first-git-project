import Dodaj_kontakt
import Edytuj_kontakt

print("Ksiazka Telefoniczna")
print("Wybierz numer z mozliwych ponizej:")
print("1.Lista kontaktow")
print("2.Dodaj kontakt")
print("3.Edytuj kontakt")
print("4.Usun kontakt")
x=input("Co wybierasz: ")
f=open("Ksiazka Telefoniczna","a+")

if x=='1':
    Edytuj_kontakt.pout_listy_kontaktow()
elif x=='2':
    nr_tele = Dodaj_kontakt.dodaj_nr_tel()
    f.write("\n"+nr_tele+"\n")

    imie=Dodaj_kontakt.dodaj_imie()
    f.write(imie+"\n")

    nazwisko=Dodaj_kontakt.dodaj_nazwisko()
    f.write(nazwisko)

elif x=='3':
    Edytuj_kontakt.edytuj_kontakt_main()
elif x=='4':
    Edytuj_kontakt.usuwanie_kontaktu()
f.close()