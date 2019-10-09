"""
How program works:
Program counts amount of line from txt file next adds values those lines to general array(arr_general)
then sorts the values from the arr_general list into individual assigned to the appropriate
information (arr_phone_number,arr_name,arr_surname)
Then shows information from those lists for user
if user input some changes then the data he changed is replaced with the new ones one the same positions in lists
Then the entire contents of the txt file are deleted and the values from the list are rewritten to the file
"""

import Add_contact
import Edit_contact

print("Phone Book")
while True:
    print("\nChoose a number from the option below:")
    print("1.List of contacts")
    print("2.Add contact")
    print("3.Edit contact")
    print("4.Delete contact")
    print("5.Make a call")
    print("\nEnter 'q' if you want to leave from program")
    x = input("Your choice: ")
    if x=='1':
        with open("Phone Book.txt", "a+") as f:
            Edit_contact.show_contacts()
    elif x=='2':
        with open("Phone Book.txt", "a+") as f:
            phone_number = Add_contact.add_a_phone_number()
            f.write("\n" + phone_number + "\n")

            name=Add_contact.add_a_name()
            if name==' ':
                name=phone_number
            f.write(name + "\n")

            surname=Add_contact.add_a_surname()
            f.write(surname)
            print("Contact has been added successful\n")
    elif x=='3':
        with open("Phone Book.txt", "a+") as f:
            Edit_contact.edit_contact_main()

    elif x=='4':
        with open("Phone Book.txt", "a+") as f:
            Edit_contact.delete_contact()
    elif x=='5':
        Edit_contact.call_a_contact()

    elif x=='q':
        break
    else:
        print("It is not possible")
        continue
    with open("Phone Book.txt", "a+") as f:
        Edit_contact.delete_list_arr_gen()
