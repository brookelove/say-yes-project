# from tabulate import tabulate
import table_and_text
import string

DRESSES = []
VENUES = []
BUDGET = {}


# def generate_table(list_of_dict):
#     # print tables for the information given that is a list of dictionaries
#     return tabulate(list_of_dict, headers='keys',
#                     tablefmt="fancy_grid")
def check_for_dollar(num):
    num = num.translate(str.maketrans('', '', string.punctuation))
    return num
    # for letter in num:
    #     if letter in string.punctuation:
    #         num = num.replace(letter, "")
    #     return num

    # if "$" == letter:
    #     # print("$")
    #     string.replace(letter, '')

    # return string


# print(check_for_dollar("$190"))
# print(check_for_dollar("$190,000"))


def dresses():
    # new_dress = []
    print("Great lets get some information to get you started on adding dress information!")
    dress_length = input(
        "What's the length of your dress?(mini, midi, floor length, ankle)\n")
    dress_type = input(
        "What's body type is  of your dress? For example there is mermaid, ballgown, column, and more\n")
    lace = input("Is the dress your looking at lace (Y/N)?\n")
    beaded = input("Is the dress your looking at beaded?(Y/N)\n")
    designer = input("What designer makes your potenital dress?\n")
    price = input("How much does this dress cost?\n")
    new_dress = {
        '': len(DRESSES) + 1,
        'Length': dress_length,
        'Type': dress_type,
        'Lace': lace,
        'Beaded': beaded,
        'Designer': designer,
        'Price': price
    }
    # new_dress.append(dress_length)
    # new_dress.append(dress_type)
    # new_dress.append(lace)
    # new_dress.append(beaded)
    # new_dress.append(company)
    # new_dress.append(shop)
    # print(new_dress)
    DRESSES.append(new_dress)
    # new_dress.clear()
    # make the counter have for the dictionary value


def venue():
    #     new_venue = []
    print("Lets make that list of venues!")
    venue_loc = input("Where is this venue?\n")
    venue_i_o = input("Is it indoor or outdoor?\n")
    vendors = input("Do they provide everything?(Y/N)\n")
    price = input("How much does this venue cost?\n")
    new_venue = {
        '': len(VENUES) + 1,
        'Location': venue_loc,
        'Indoor/Outdoor': venue_i_o,
        'What do they provide': vendors,
        'Price': price
    }
    VENUES.append(new_venue)
#     # include if else for Y/Ns
#     # maybe add an if else condition to have what they do not include
#     # if statemnt to add dollar sign
#     new_venue.append(venue_i_o)
#     new_venue.append(vendors)
#     new_venue.append(venue_loc)
#     new_venue.append(price)
#     # print(new_venue)
#     VENUES[len(VENUES)] = new_venue
    # new_venue.clear()


def budget():
    print("It is always great to get a new budget!")
    total = input("Whats your total budget for you wedding?\n $")
    venue = input("What's your budget for your venue?\n$")
    food = input("What's your budget for your food?\n$")
    dress = input("Whats your budget for the dress?\n$")
    tux = input("Whats your budget for the tux?\n$")
    wedding_night = input(
        "Whats your budget for the Hotel stay of the wedding night?\n$")
    photo = input(
        "Whats your budget for your photographer and/or videographer?\n$")
    hair_and_makeup = input("Whats your budget for the hair and makeup?\n$")

    total_fl = check_for_dollar(total)
    venue_fl = check_for_dollar(venue)
    food_fl = check_for_dollar(food)
    dress_fl = check_for_dollar(dress)
    tux_fl = check_for_dollar(tux)
    wedding_night_fl = check_for_dollar(wedding_night)
    photo_fl = check_for_dollar(photo)
    hair_and_makeup_fl = check_for_dollar(hair_and_makeup)

    total_price = float(food_fl) + float(venue_fl) + float(dress_fl) + float(
        tux_fl) + float(wedding_night_fl) + float(hair_and_makeup_fl) + float(photo_fl)
    leftover = float(total_fl) - total_price

    # print(total_budg)
    BUDGET["Total budget"] = f"${total_fl}"
    BUDGET["Venue budget"] = f"${venue_fl}"
    BUDGET["Food budget"] = f"${food_fl}"
    BUDGET["Dress budget"] = f"${dress_fl}"
    BUDGET["Tux budget"] = f"${tux_fl}"
    BUDGET["Hotel Stay"] = f"${wedding_night_fl}"
    BUDGET["Photographer budget"] = f"${photo_fl}"
    BUDGET["Hair and Makeup budget"] = f"${hair_and_makeup_fl}"
    BUDGET["Budget Remaining "] = f"${leftover}"


def generate_table_and_text(user_info):
    # all_info = set(user_info, VENUES, BUDGET, DRESSES)
    print("Taking all information and getting it together...")
    print("Generating Text...")
    # table_and_text(all_info)
    # where I would use the class to generate an output file


def menu(user_info):
    choice = False
    # dress_headers = ['Length', 'Type', 'Lace', 'Beaded', 'Company', 'Shop']
    # venue_headers = {'Location',
    #                  'Indoor/Outdoor', 'What Do they Provide', 'Price'}
    # DRESSES[len(DRESSES)] = dress_headers
    # print(menu_choice)
    user_results = table_and_text.UserResults(user_info)
    # names = user_info
    print(
        f"Hi {user_info[0]}, lets start making your list for you and {user_info[0]} special day!")
    while not choice:
        menu_choice = input(
            "Please choose the corresponding letter from one of the following to enter your new idea:\n A.Dresses\n B.Venue\n C.Budget\n D.See All\n E.Exit\n ")
        if menu_choice.upper() == 'E':
            choice = True
            print(user_results.__repr__())
            lines = [f"{user_results.user_info_print()}", f"The amount of dresses you made into a list {str(len(DRESSES))}",
                     f"{user_results.generate_table(DRESSES)}", f"The amount of venues you made into a list {str(len(VENUES))}", f"{user_results.generate_table(VENUES)}", "The budget you made",  f"{user_results.generate_table([BUDGET])}"]
            user_results.text_file(lines)
        elif menu_choice.upper() == 'A':
            # DRESSES[len(DRESSES)] = dress_headers
            dresses()
            # print(DRESSES)
            print(user_results.generate_table(DRESSES))
            # generate_table(DRESSES)
            # print(tabulate(DRESSES, headers="keys", tablefmt="fancy_grid"))
            # print(DRESSES.values())
            # print(
            #     tabulate([DRESSES.values()], headers=dress_headers))
            # print(
            # tabulate([DRESSES.values()], headers=dress_headers))
            # print(
            #     tabulate([(k,) + v for k, v in DRESSES.items()], headers=dress_headers))
            #       tablefmt="fancy_grid"))
            # -------------------------------------------------
            # print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Length', 'Type', 'Lace',
            #                                                          'Beaded', 'Company', 'Shop'))
            # for key, value in DRESSES.items():
            #     length, dress_type, lace, beaded, company, shop = value
            #     print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(length, dress_type, lace,
            #                                                              beaded, company, shop))
            # ------------------------------------------------------
        elif menu_choice.upper() == 'B':
            venue()
            # generate_table(VENUES)
            print(user_results.generate_table(VENUES))
            # print(tabulate(VENUES, headers='keys',
            #       tablefmt="fancy_grid"))
        #     print("{:<10} {:<10} {:<10} {:<10}".format(
        #         'Location', 'Indoor/Outdoor', 'What Do They Provide', 'Price'))
        #     for key, value in VENUES.items():
        #         location, i_o, provide, price = value
        #         print("{:<10} {:<10} {:<10} {:<10}".format(
        #             location, i_o, provide, price))
            # print(tabulate([VENUES], headers=venue_headers,
            #       tablefmt="fancy_grid"))
        elif menu_choice.upper() == 'C':
            budget()
            # print(BUDGET)
            # generate_table([BUDGET])\
            print(user_results.generate_table([BUDGET]))
            # table_and_text.UserResults.generate_table(list(BUDGET))
            # print(tabulate([BUDGET], headers='keys',
            #       tablefmt="fancy_grid"))
            # print(tabulate(list(BUDGET)))
        elif menu_choice.upper() == 'D':
            print("Here is What you've entered: ")
            print(f"Budget:\n{user_results.generate_table([BUDGET])}")
            print(
                f"Dresses:\nTotal Amount entered: {len(DRESSES)}\n{user_results.generate_table(DRESSES)}")
            print(
                f"Venues:\nTotal Amount entered: {len(VENUES)}\n{user_results.generate_table(VENUES)}")
        else:
            print("Please Try entering one of the choices listed above. If you are trying to exit this menu, print 'D'.")
            # menu()


# menu()
