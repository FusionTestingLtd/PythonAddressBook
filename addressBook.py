# Menu:
#   Show entire address book
#   Add an address
#   (search for entry)

#  get the address to add from the user:


# Add address to file
# Show the address that was added

def menu():
    while True:
        try:
            print("\n1. Show Address Book")
            # print("2. (Search for Entry)")
            print("2. Add an Address")
            print("3. Exit")
            choice = int(input("What would you like to do? "))
            if choice < 1 or choice > 3:
                print("Invalid selection\n")
                continue
            else:
                return choice
        except ValueError:
            print("Invalid selection\n")
            continue


def address_input():
    #  -------- NAME INPUT --------------
    while True:
        try:
            name = input("Full name: ").split()

            if len(name) == 2 and name[0].isalpha() and name[1].isalpha():
                first_name = name[0]
                middle_name = "-"
                last_name = name[1]
                break
            elif len(name) == 3 and name[0].isalpha() and name[1].isalpha():
                first_name = name[0]
                middle_name = name[1]
                last_name = name[2]
                break
            else:
                print("Err-2 Please Enter first and last name separated by space\n")
                continue
        except ValueError:
            print("Err-1 Shouldn't be able to get here\n")
            continue
    # --------- HOUSE NUMBER / NAME INPUT -----------
    house_number = input("House Name or Number: ")
    # --------- STREET INPUT -------------
    while True:
        try:
            street = input("Street: ")
            if street.replace(" ", "").isalpha():
                break
            else:
                print("Err-4 Streets cannot contain numbers or special characters\n")
        except ValueError:
            print("Err-3 shouldn't be able to get here!\n")
            continue
    # -------- TOWN INPUT -------------
    while True:
        try:
            town = input("Town: ")
            if town.isalpha():
                break
            else:
                print("Err-5 Towns cannot contain numbers\n")
                continue
        except ValueError:
            print("Err-6 shouldn't be able to get here!\n")
            continue
    # -------- POSTCODE INPUT -------------
    while True:
        try:
            postcode = input("PostCode: ").replace(" ", "")
            if postcode.isalnum():
                break
            else:
                print("Err-7 Invalid postcode")
                continue
        except ValueError:
            print("Err-8 shouldn't be able to get here!\n")
            continue
    # -------- PHONE NUMBER INPUT -------------
    while True:
        try:
            phone_number = input("Phone Number: ")
            if phone_number.isnumeric() and len(phone_number) == 11:
                break
            else:
                print("Err-9 Invalid Phone number")
                continue
        except ValueError:
            print("Err-10 shouldn't be able to get here!\n")
            continue

    # format CSV string to return
    address = [first_name, middle_name, last_name, house_number, street, town, postcode, phone_number]
    i = 0
    data = ""
    while i < len(address):
        data = data + "{}{}".format(address[i], ",")
        i = i + 1

    # Display confirmation statement to the user..
    print("{} {} {} {}".format("Address entry for [", first_name, last_name, "] has been successful!"))
    return data


def format_input_from_file(file_input):
    x = file_input.replace(",", "    ")
    return x


def file_length():
    with open("Address.txt", "r") as data:
        line = data.readline()
        count = 0
        while line:
            line = data.readline()
            count = count + 1
        data.close()
    return count


# --------------- Main Program! -----------------
while True:
    menu_choice = menu()
    if menu_choice == 2:
        file = open("Address.txt", "a+")
        file_len = file_length()
        if file_len == 0:
            file.write("{}  {}  {}  {}  {}  {}  {}  {}".format("(FirstName", "MiddleName", "Lastname",
                                                               "House Name/No", "Street", "Town", "Postcode", "Phone)\n"))
            file.write("{}{}".format(str(address_input()), "\n"))
            file.close()
        else:
            file.write("{}{}".format(str(address_input()), "\n"))
            file.close()

    elif menu_choice == 1:
        while True:
            try:
                file = open("Address.txt", "r")  # open the file
                address_line = format_input_from_file(file.readline())  # read the first line
                i = 1  # set a counter
                while address_line:  # while there is a line to read
                    print(address_line.strip('\n'))  # print it - without the extra LF.
                    address_line = format_input_from_file(file.readline())  # read the next line
                    i = i + 1  # increment the counter
                file.close()  # close the file.
                break
            except IOError:
                print("\nThere is no Address book! -- Please add an address.\n")
                break
    elif menu_choice == 3:
        exit()
