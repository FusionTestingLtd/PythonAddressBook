
# add ability to create a new addressbook or select existing one.

from file_functions import write_to_file, read_from_file, search_file, delete_record, file_length
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
        search_file(input("\nSearch for: "))
    elif menu_choice == 4:
        while True:
            try:
                rec_to_del = int(input("Record to delete:"))
                if rec_to_del > file_length() - 1 or rec_to_del < 1:
                    print("\nNo Such Record to delete, Try the search.")
                else:
                    delete_record(rec_to_del)
            except ValueError:
                print("\nPlease valid Record ID")
                continue
            else:
                break
        # delete_record(int(input("Record to delete:")))

    elif menu_choice == 5:
        exit()
