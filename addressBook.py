
# add ability to create a new addressbook or select existing one.

from file_functions import write_to_file, read_from_file, search_file
from functions import menu

# -----------------------------------------------
# --------------- Main Program! -----------------
# -----------------------------------------------
while True:
    menu_choice = menu()
    if menu_choice == 2:
        write_to_file()
    elif menu_choice == 1:
        read_from_file()
    elif menu_choice == 3:
        search_file(input("Search for: "))
    elif menu_choice == 4:
        exit()
