# Menu:
#   Show entire address book
#   Add an address
#   (search for entry)

#  get the address to add from the user:


# Add address to file
# Show the address that was added
# add ability to create a new addressbook or select existing one.
from file_functions import write_to_file, read_from_file
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
        exit()
