from formatting_functions import format_input_from_file
from functions import address_input


# -------------------------
#   WRITE DATA TO FILE
# -------------------------
def write_to_file():
    file = open("Address.txt", "a+")
    file_len = file_length()
    if file_len == 0:
        file.write("{}  {}  {}  {}  {}  {}  {}  {}".format("[FirstName]", "[MiddleName]", "[Lastname]",
                                                           "[House Name/No]", "[Street]", "[Town]", "[Postcode]", "[Phone]\n"))
        file.write("{}{}".format(str(address_input()), "\n"))
        file.close()
    else:
        file.write("{}{}".format(str(address_input()), "\n"))
        file.close()


# -------------------------
#   READ DATA FROM FILE
# -------------------------
def read_from_file():
    if file_length() < 2:
        print("---- Empty File! -----")
    else:
        while True:
            try:
                file = open("Address.txt", "r")  # open the file
                address_line = format_input_from_file(file.readline())  # read the first line
                i = 1  # set a counter
                while address_line:  # while there is a line to read
                    if i == 1:
                        print(address_line.strip('\n'))  # print it - without the extra LF.
                        address_line = format_input_from_file(file.readline())
                        i = i + 1
                    else:
                        print("{} {}".format([i - 1], address_line.strip('\n')))  # print it - without the extra LF.
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


# -------------------------
#   SEARCH FILE FOR X
# -------------------------
def search_file(search_term):
    search_term = str(search_term).lower()
    print("{} {}".format("\nSearched for:", search_term))
    with open("Address.txt", "r") as data:
        line = data.readline().lower()  # line is str
        line = data.readline().lower()  # line is str
        i = 1
        while line:
            if search_term not in line:
                pass
            else:
                print("{} {}".format([i], format_input_from_file(line)))
            line = data.readline().lower()
            i = i + 1
        data.close()


# -------------------------
#   DELETE ENTRY FROM FILE
# -------------------------
def delete_record(record_to_del):  # validation on rec to del
    lines = []
    with open("Address.txt", "r") as data:
        line = data.readline()
        i = 0
        while line:
            lines.append(line)
            line = data.readline()
            i = i + 1
        data.close()
    print("{} {}".format("\nDeleting Record:", record_to_del))
    print(format_input_from_file(lines[record_to_del]))
    with open("Address.txt", "w") as data:
        x = 0
        while x < len(lines):
            if x == record_to_del:
                x = x + 1
            else:
                data.write(lines[x])
                x = x + 1
        print("{} {} {}".format("Record:", record_to_del, "deleted!"))
        data.close()
