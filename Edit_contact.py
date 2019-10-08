import Add_contact

arr_emg_num=("997", "Police", " ", "998", "Fire department", " ", "999", "Emergency service", " ")
arr_name = []  # List of name
arr_surname = []  # List of surname
arr_phone_number = []  # A list of phone numbers
arr_AoL = []  # List with amount of line
arr_general = []  # General list with every information from lines

def adding_constants_to_the_list():
    """The function which is responsible for not being able to delete emergency numbers"""
    with open("Phone Book.txt",mode='a+') as w:
        if amount_of_line()==0 or amount_of_line()==False:
            k=0
            while k <= len(arr_emg_num):
                if k != 8:
                    w.write(arr_emg_num[k] + '\n')
                else:
                    w.write(arr_emg_num[k])
                    break
                k = k + 1
        w.seek(0)

def amount_of_line():
    """Counts the number of lines in the txt file"""
    i=0
    with open("Phone Book.txt",mode='r') as f:
        for i,l in enumerate(f):
            pass
        amount_of_line=i
    return amount_of_line

def adding_to_the_list(lines):
    """Loop removal '\n' character and adding words from specified line to list"""
    sum = 0
    r=open("Phone Book.txt",mode="a+")
    r.seek(0)
    i=int(0)
    while i<=lines:
        arr_AoL.append(len(r.readline())) # Counts the numbers of characters from single line and adds those value to --
        i=i+1                             # the list
    i=int(0)
    r.seek(0)

    while i<=lines:
        if i==lines:
            read=r.read(arr_AoL[i])
        else:
            read=r.read(arr_AoL[i] - 1)
        arr_general.append(read) # Adds word without \n to the list
        sum= sum + arr_AoL[i]
        r.seek(sum+i+1)
        i=i+1
    r.close()

def sorting_to_the_list():
    """Block that assign a number, first and last name, respectively, to the appropriate lists"""
    adding_to_the_list(amount_of_line())
    a,b,c=0,1,2
    That_is_true=False
    while a <= len(arr_AoL):
        try:
            if arr_general[a] in arr_phone_number:
                break
            else:
                That_is_true = True
                arr_phone_number.append(arr_general[a])
                a = a + 3
        except IndexError:
            break
    while b <= len(arr_AoL):
        if That_is_true==True:
            try:
                arr_name.append(arr_general[b])
                b = b + 3
            except IndexError:
                break
        else:
            break
    while c <= len(arr_AoL):
        if That_is_true==True:
            try:
                arr_surname.append(arr_general[c])
                c = c + 3
            except IndexError:
                break
        else:
            break

def pout_list_of_contacts():
    """ Shows contacts in program """
    sorting_to_the_list()
    i=int(0)
    while i+1<=len(arr_phone_number):
        try:
            print(str(i+1) +". " + arr_name[i] + " " + arr_surname[i] + " ( " + arr_phone_number[i] + " )")
        except IndexError:
            break
        i=i+1

def delete_contact_list():
    """Block of code that is responsible for deleting list ( to re-enter it in the file )"""
    with open ("Phone Book.txt","r+") as f:
        f.seek(0)
        for index_of_line,line in enumerate(f):
            if index_of_line>8:
                del line

def delete_position(which_contact):
    """Deleting specific position in the lists"""
    arr_phone_number.remove(arr_phone_number[which_contact - 1])
    arr_name.remove(arr_name[which_contact - 1])
    arr_surname.remove(arr_surname[which_contact - 1])

    arr_general.remove(arr_general[which_contact * 3 - 1])
    arr_general.remove(arr_general[which_contact * 3 - 2])
    arr_general.remove(arr_general[which_contact * 3 - 3])

def re_adding_to_the_list():
    """Writing information from the list(arr_general) to a file """
    with open("Phone Book.txt", 'w') as f:
        for number_of_index, index in enumerate(arr_general):
            if number_of_index!=0:
                f.write("\n")
            f.write("{}".format(index))

def delete_contact():
    """Deleting specifed contact"""
    pout_list_of_contacts()
    print("\nWhich contact do you want to delete: ",end='')
    user_choice=int(input())
    delete_position(user_choice)
    re_adding_to_the_list()

def delete_list_arr_gen():
    "function that is responsible for deleting every element of main array-'arr_general' "
    i=len(arr_general)-1
    while i>=0:
        del(arr_general[i])
        i-=1

def edit_contact_main():
    """Main function responsible for 'List of contacts', 'Edit contact', 'Delete contact' in main file"""
    r=open("Phone Book.txt", mode="a+")
    adding_constants_to_the_list()
    pout_list_of_contacts()

    print("\nWhich contact do you want to edit?: ", end='')
    choose=int(input(""))

    delete_position(choose)

    print("Enter again contact")
    """It introduces a new position in place of the previous one that has been changed"""
    arr_phone_number.insert(choose - 1, Add_contact.add_a_phone_number())
    arr_name.insert(choose - 1, Add_contact.add_a_name())
    arr_surname.insert(choose - 1, Add_contact.add_a_surname())

    arr_general.insert(choose * 3 - 3, arr_phone_number[choose - 1])
    arr_general.insert(choose * 3 - 2, arr_name[choose - 1])
    arr_general.insert(choose * 3 - 1, arr_surname[choose - 1])

    delete_contact_list()

    re_adding_to_the_list()
    r.close()
