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


add_another = input("enter your choice:\n1) add a contact\n2) remove a"
                    " contact\n3) list contacts\n4) Exit\n: ")

while add_another != "4":
    contact_first_name = input("first name: ")
    contact_last_name = input("last name: ")
    contact_phone = input("phone number: ")
    clear()
    contact_list += [contact(contact_first_name, contact_last_name,
                             contact_phone)]
    add_another = input("enter your choice:\n1) add a contact\n2) remove a"
                        " contact\n3) list contacts\n4) Exit\n: ")

for i in contact_list:
    print(i.first_name)
