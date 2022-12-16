# class OutOfBounds (Exception):
# use set in here
from tabulate import tabulate
#     pass


class UserResults:
    # def __init__(self, user_name, part_name, location, date:
    #     self.__name = user_name
    #     seld.
    def __init__(self, user_name, partner, date, dresses, venues, budget):
        # need to have two private and public
        self.user_name = user_name
        self.partner = partner
        # self.__location = location
        self.date = date
        self.__dresses = dresses
        self.__venues = venues
        self.__budget = budget

    def get_personal_info(self):
        return (self.__user_name, self.__partner, self.location, self.date)

    def __text_file():
        # going to write the data to another file as an output
        pass

    def user_info_print(self):
        # with print out the name, a partners name, and the date which is a tuple
        return print(f"Thank you {self.user_name} for using Say Yes, we hope that you and {self.partner}'s day goes fantasic and smooth on {self.date}!")

    def user_results(list_of_dict):
        # print tables for the information given that is a list of dictionaries
        return tabulate(list_of_dict, headers='keys',
                        tablefmt="fancy_grid")

    def __len__(self):  # magic class
        total_items = {len(self.__dresses), len(self.__venues)}
        return total_items

    def __repr__(self):
        return ("Thanks for Using our program we wanted you to have these files as a text! ")
