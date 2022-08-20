import os


def clear():
    lambda: os.system('clear')


contactList = []


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
    choice = input(("Search by? (F)irst name, (L)ast name or \
                    (P)hone number\n" +
                   "Enter F, L, or P: ")).casefold
    if choice == 'f':
        f_name = input("enter first name to search: ")
        for index, item in enumerate(contactList):
            if item.first_name == f_name:
                contactList.pop(index)
    elif choice == 'l':
        l_name = input("enter first name to search: ")
        for index, item in enumerate(contactList):
            if item.last_name == l_name:
                contactList.pop(index)
    elif choice == 'p':
        p_number = input("enter first name to search: ")
        for index, item in enumerate(contactList):
            if item.phone_number == p_number:
                contactList.pop(index)


user_choice = 0

# # begin test contacts
contactList.append(contact('user1f', 'user1l', 123456))
contactList.append(contact('user2f', 'user2l', 234567))
contactList.append(contact('user3f', 'user3l', 345678))
# # end test contacts

while user_choice != "4":
    clear()
    user_choice = input(
        """enter your choice:
1) add a contact
2) remove a contact
3) list contacts
4) Exit
 """)

    if user_choice == "1":
        contactList += addContact()

    elif user_choice == "2":
        removeContact()

    elif user_choice == "3":
        for item in contactList:
            print(item.first_name)
        input("press enter to continue")

for i in contactList:
    print("{0} {1}".format(i.first_name, i.last_name))
