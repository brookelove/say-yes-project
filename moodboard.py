
def dresses():
    print("Great lets get some information to get you started on adding dress information!")


def venue():
    print("Lets make that list of venues!")


def budget():
    print("It is always great to get a new budget!")


def menu():
    choice = False
    # print(menu_choice)
    while not choice:
        menu_choice = input(
            "Please choose the corresponding letter from one of the following to enter your new idea:\n A.Dresses\n B.Venue\n C.Budget\n D.Exit\n ")
        if menu_choice.upper() == 'D':
            choice = True
            return menu_choice
        elif menu_choice.upper() == 'A':
            dresses()
        elif menu_choice.upper() == 'B':
            venue()
        elif menu_choice.upper() == 'C':
            budget()
        else:
            print("Please Try entering one of the choices listed above. If you are trying to exit this menu, print 'D'.")
            menu()


# menu()
