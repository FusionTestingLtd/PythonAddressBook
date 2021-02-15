
# -------------------------
#   FORMAT DATA FOR FILE ENTRY
# -------------------------
def format_to_csv(first_name, middle_name, last_name, house_number, street, town, postcode, phone_number):
    address = [first_name, middle_name, last_name, house_number, street, town, postcode, phone_number]
    i = 0
    data = ""
    while i < len(address):
        data = data + "{}{}".format(address[i], ",")
        i = i + 1
    return data


# -------------------------
#   FORMAT DATA FROM FILE
# -------------------------
def format_input_from_file(file_input):
    x = file_input.replace(",", "    ")
    return x
