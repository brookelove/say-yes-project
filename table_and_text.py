# class OutOfBounds (Exception):
# use set in here
from tabulate import tabulate
#     pass


class UserResults:
    # def __init__(self, user_name, part_name, location, date:
    #     self.__name = user_name
    #     seld.
    def __init__(self, user_info):
        # need to have two private and public
        self.user_name = user_info[0]
        self.partner = user_info[1]
        self.__date = user_info[2]
        # self.__dresses = dresses
        # self.__venues = venues
        # self.__budget = budget

    def generate_table(self, list_of_dict):
        # print tables for the information given that is a list of dictionaries
        return tabulate(list_of_dict, headers='keys',
                        tablefmt="fancy_grid")

    def __get_personal_info(self):
        return f"Wow you created sufh a great list {self.user_name}! Time to relax and lay back."

    def text_file(self, lines):
        # going to write the data to another file as an output
        with open('say_yes.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
        return print(f"We have generated your list. Please locate the say_yes.txt file!")

    def user_info_print(self):
        # with print out the name, a partners name, and the __date which is a tuple
        return (f"{self.__get_personal_info()}\nThank you {self.user_name} for using Say Yes, we hope that you and {self.partner}'s day goes fantasic and smooth on {self.__date}!")
        # return

    def __len__(self):  # magic class
        total_items = len(self.__dresses) + len(self.__venues)
        return total_items

    def __repr__(self):
        return ("Thanks for Using our program we wanted you to have these files as a text! ")


# UNIT TEST ONE ====================================
# user_results = ("Daphne", "Fred", "10/25/2056")
# dresses = [
#     {
#         'Length': 'midi',
#         'Type': 'ballgown',
#         'Lace': 'Y',
#         'Beaded': 'N',
#         'Designer': 'Daphne Blake',
#         'Price': 0
#     },
#     {
#         'Length': 'midi',
#         'Type': 'ballgown',
#         'Lace': 'N',
#         'Beaded': 'Y',
#         'Designer': 'The Hex Girls',
#         'Price': 1800
#     },
# ]
# venues = [
#     {

#         'Location': "Spooky Island",
#         'Indoor/Outdoor': "outdoor",
#         'Do they provide everthing': 'Yes',
#         'Price': "1500"
#     },
#     {

#         'Location': "Haundted House",
#         'Indoor/Outdoor': "Indoor",
#         'Do they provide everything': 'No',
#         'Price': "100"
#     },
# ]
# budget = [{
#     "total ": "100000",
#     "venue ": "15000",
#     "food": "800",
#     "dress ": "0",
#     "tux ":  "80",
#     "Hotel Stay ": "800",
#     "Photographer": "180",
#     "Hair and Makeup ": "800",
#     " Remaining ": "20"
# }]
# user = UserResults(user_results)
# print("here 1")
# print(user.user_info_print())
# print(user.get_personal_info())
# # print(venues)
# print("here")
# print(user.generate_table(venues))
# print(user.generate_table(budget))
# print(user.generate_table(dresses))
# UNIT TEST TWO ===========================================
# user_results = ("Shaggy", "Velma", "6/25/2024")
# dresses = [
#     {
#         'Length': 'tea',
#         'Type': 'A-line',
#         'Lace': 'Y',
#         'Beaded': 'N',
#         'Designer': 'Daphne Blake',
#         'Price': 0
#     },
#     {
#         'Length': 'floor length',
#         'Type': 'column',
#         'Lace': 'N',
#         'Beaded': 'Y',
#         'Designer': 'The Hex Girls',
#         'Price': 3800
#     },
# ]
# venues = [
#     {

#         'Location': "Library",
#         'Indoor/Outdoor': "Indoor",
#         'Do they provide everythng': 'Y',
#         'Price': "50"
#     },
#     {

#         'Location': "Burger Shack",
#         'Indoor/Outdoor': "Indoor",
#         'Do they provide everything': 'N we need a place ot get married',
#         'Price': "10"
#     },
# ]
# budget = [{
#     "total ": "200000",
#     "venue ": "500",
#     "food": "800",
#     "dress ": "5000",
#     "tux ":  "80",
#     "Hotel Stay ": "800",
#     "Photographer": "180",
#     "Hair and Makeup ": "800",
#     " Remaining ": "20"
# }]
# user = UserResults(user_results)
# print(user.user_info_print())
# print(user.get_personal_info())
# print(venues)
# print(user.generate_table(venues))
# print(user.generate_table(budget))
# print(user.generate_table(dresses))
