from tabulate import tabulate

DRESSES = {}
VENUES = {}
BUDGET = {}


def dresses():
    new_dress = []
    print("Great lets get some information to get you started on adding dress information!")
    dress_length = input(
        "What's the length of your dress?(mini, midi, floor length, ankle)\n")
    dress_type = input(
        "What's body type is  of your dress? For example there is mermaid, ballgown, column, and more\n")
    lace = input("Is the dress your looking at lace (Y/N)?\n")
    beaded = input("Is the dress your looking at beaded?(Y/N)\n")
    company = input("What company makes your potenital dress\n")
    shop = input("How much does this dress cost?\n")

    new_dress.append(dress_length)
    new_dress.append(dress_type)
    new_dress.append(lace)
    new_dress.append(beaded)
    new_dress.append(company)
    new_dress.append(shop)
    print(new_dress)
    DRESSES[len(DRESSES) + 1] = new_dress
    # new_dress.clear()
    # make the counter have for the dictionary value


# def venue():
#     new_venue = []
#     print("Lets make that list of venues!")
#     venue_loc = input("Where is this venue?\n")
#     venue_i_o = input("Is it indoor or outdoor?")
#     vendors = input("Do they provide everything?(Y/N)\n")
#     price = {"How much does this venue cost?"}
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
    total_budg = input("Whats your total budget for you wedding?\n")
    print(total_budg)
    BUDGET["total budget"] = total_budg
    venue_budg = input("What's your budget for your venue?\n")
    BUDGET["venue budget"] = venue_budg
    food_budg = input("What's your budget for your food?\n")
    BUDGET["food budget"] = food_budg
    dress_budg = input("Whats your budget for the dress?\n")
    BUDGET["dress budget"] = dress_budg
    tux_budg = input("Whats your budget for the tux?\n")
    BUDGET["tux budget"] = tux_budg
    wedding_night_budg = input("Whats your budget for the Wedding Night?\n")
    BUDGET["Wedding Night budget"] = wedding_night_budg
    photo_budg = input(
        "Whats your budget for your photographer and/or videographer?\n")
    BUDGET["Photographer budget"] = photo_budg
    hair_and_makeup = input("Whats your budget for the hair and makeup?\n")
    BUDGET["Hair and Makeup budget"] = hair_and_makeup
    total_price = float(food_budg) + float(venue_budg) + float(dress_budg) + float(
        tux_budg) + float(wedding_night_budg) + float(photo_budg) + float(hair_and_makeup)
    leftover = float(total_budg) - total_price
    BUDGET["Budget Remaining "] = leftover


def generate_table_and_text():
    print("Generating Table...")


def menu(user_info):
    choice = False
    dress_headers = ['', 'Length', 'Type', 'Lace', 'Beaded', 'Company', 'Shop']
    venue_headers = {'Location',
                     'Indoor/Outdoor', 'What Do they Provide', 'Price'}
    # DRESSES[len(DRESSES)] = dress_headers
    # print(menu_choice)
    print(
        f"Hi {user_info[0]}, lets start making your list for you and {user_info[1]} special day!")
    while not choice:
        menu_choice = input(
            "Please choose the corresponding letter from one of the following to enter your new idea:\n A.Dresses\n B.Budget\n C.Exit\n ")
        if menu_choice.upper() == 'C':
            choice = True
            return print(user_info)
        elif menu_choice.upper() == 'A':
            dresses()
            # print(DRESSES)
            print(DRESSES.values())
            print(
                tabulate([DRESSES.values()], headers=dress_headers))
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
        # elif menu_choice.upper() == 'B':
        #     venue()
        #     print("{:<10} {:<10} {:<10} {:<10}".format(
        #         'Location', 'Indoor/Outdoor', 'What Do They Provide', 'Price'))
        #     for key, value in VENUES.items():
        #         location, i_o, provide, price = value
        #         print("{:<10} {:<10} {:<10} {:<10}".format(
        #             location, i_o, provide, price))
            # print(tabulate([VENUES], headers=venue_headers,
            #       tablefmt="fancy_grid"))
        elif menu_choice.upper() == 'B':
            budget()
            # print(BUDGET)
            print(tabulate([BUDGET], headers='keys',
                  tablefmt="fancy_grid"))
            # print(tabulate(list(BUDGET)))
        else:
            print("Please Try entering one of the choices listed above. If you are trying to exit this menu, print 'D'.")
            # menu()


# menu()
