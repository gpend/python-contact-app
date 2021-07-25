import os


def clear():
    lambda: os.system('clear')


contact_list = []


class contact:
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def print_contact(self):
        print("name: {0} {1}\nPhone number: {2}".format(self.first_name,
              self.last_name, self.phone_number))


def addContact():
    contact_first_name = input("first name: ")
    contact_last_name = input("last name: ")
    contact_phone = input("phone number: ")
    # clear()
    return [contact(contact_first_name, contact_last_name, contact_phone)]


def removeContact():
    choice = input("Search by? (F)irst name, (L)ast name or (P)hone number\nEnter F, L, or P: ")
    if choice == "F":
        pass
    elif choice == "L":
        pass
    elif choice == "P":
        pass


add_another = 0


while add_another != "4":
    add_another = input(
"""enter your choice:
1) add a contact
2) remove a contact
3) list contacts
4) Exit
 """)
    if add_another == "1":
        contact_list += addContact()
    elif add_another == "2":
        print("sorry, not implemented yet")
        removeContact()
    elif add_another == "3":
        print("sorry, not implemented yet")


for i in contact_list:
    print("{0} {1}".format(i.first_name, i.last_name))
