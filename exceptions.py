class OutOfBounds(Exception):  # has to be only 3 items in the list
    pass


class NonValdMonth(Exception):  # has to be between 0 and 1
    pass


class NotValidDay(Exception):  # less than or equal to 31 from 1
    pass


class NotValidYear(Exception):  # greater or equal to the current year
    pass


# class NotValidDate(Exception):  # has to be greater than this date
#     pass
