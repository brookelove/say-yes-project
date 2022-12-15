

def menu():
    choice = False
    # print(menu_choice)
    while not choice:
        menu_choice = input(
            "Please choose the corresponding letter from one of the following to enter your new idea:\n A.Dresses\n B.Venue\n C.Budget\n D.Exit\n ")
        if menu_choice.upper() == 'D':
            choice = True
            return menu_choice
        if menu_choice.upper() == 'A':
            pass
        elif menu_choice.upper() == 'B':
            pass
        elif menu_choice.upper() == 'C':
            pass
        else:
            print("Please Try entering one of the choices listed above. If you are trying to exit this menu, print 'D'.")
            menu()


menu()
