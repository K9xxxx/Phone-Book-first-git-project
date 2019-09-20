def dodaj_nr_tel():
    while True:
        _nr_tel = input("Podaj numer telefonu: ")
        if len(_nr_tel)==0:
            print("\nMusisz podac numer telefonu")
        else:
            try:                                    # Zmusza do wpisania cyfr
                _try_nr_tel = int(_nr_tel)
                break
            except ValueError:
                print("\nNumer telefonu jest niepoprawny")

    return _nr_tel

def dodaj_imie():
    _imie=input("Podaj imie: ")
    if len(_imie) == 0:
        _imie = " "
    return _imie

def dodaj_nazwisko():
    _nazwisko=input("Podaj nazwisko: ")
    if len(_nazwisko) == 0:
        _nazwisko=" "
    return _nazwisko