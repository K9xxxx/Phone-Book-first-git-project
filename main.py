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
print("Choose a number from the option below:")
print("1.List of contacts")
print("2.Add contact")
print("3.Edit contact")
print("4.Delete contact")
x=input("Your choice: ")
f=open("Phone Book.txt","a+")

if x=='1':
    Edit_contact.pout_list_of_contacts()
elif x=='2':
    phone_number = Add_contact.add_a_phone_number()
    f.write("\n" + phone_number + "\n")

    name=Add_contact.add_a_name()
    f.write(name + "\n")

    surname=Add_contact.add_a_surname()
    f.write(surname)
    print("Contact has been added successful")

elif x=='3':
    Edit_contact.edit_contact_main()
elif x=='4':
    Edit_contact.delete_contact()
f.close()