from formatting_functions import format_input_from_file
from functions import address_input


# -------------------------
#   WRITE DATA TO FILE
# -------------------------
def write_to_file():
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


# -------------------------
#   READ DATA FROM FILE
# -------------------------
def read_from_file():
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


# -------------------------
#   DETERMINE FILE LENGTH
# -------------------------
def file_length():
    with open("Address.txt", "r") as data:
        line = data.readline()
        count = 0
        while line:
            line = data.readline()
            count = count + 1
        data.close()
    return count
