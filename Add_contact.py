def add_a_phone_number():
    while True:
        _phone_number = input("Enter the phone number: ")
        with open("Phone Book.txt", "r") as f:
            array_for_drt = []
            for index in f:
                array_for_drt.append (index[0:len(index)-1])  # Adds object from file to array without '\n'
            if _phone_number in array_for_drt:  # Checks for the existence of the phone number provided
                print("Number already exist")
                continue
            else:
                if len( _phone_number )==0:
                    print("\nYou have to enter phone number")
                else:
                    try:                                    # Force to enter numbers
                        _try_phone_number = int(_phone_number)
                        break
                    except ValueError:
                        print("\nNumber of phone is invalid")

    return _phone_number

def add_a_name():
    _name=input("Enter name: ")
    if len(_name) == 0:
        _name = " "
    return _name

def add_a_surname():
    _surname=input("Enter surname: ")
    if len(_surname) == 0:
        _surname=" "
    return _surname