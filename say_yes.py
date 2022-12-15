'''
1. welcome user to the say yes project
2. then prompt user for their desired wedding date, location, your and partners name, budget
    CLASS:  
    - inform them that they can change the date later 
    - TRY / ELSE BLOCK where i am trying ot get a valid date that is greater than the current day
    - while loop to ask for a valid date until it is not needs to be in a particular format MM/DD/YYYY and compare that it has to be greater than current date
3. click on options that you want to pick [elopement, big wedding, micro wedding]
    - confirm this what they want yes / no
4. have a dictionary comprised of lists that a person can add informaiton such as venue, food, bridal shops, tux, pinterst board links, color scheme 
    - can look at a table that shows the information 
    - cna delete the data if needed (will need to add an id of sorts or can just need to get the index)
5. output a file of the list of elements that the person has added 
'''
import datetime
import exceptions
import string

TODAY = datetime.date.today()


def date_valid(d):  # USER DEFINED FUNCTION NEEDS A RETURN
    entered_date = d[0]
    # print(entered_date)
    for i in entered_date:
        if i in string.punctuation:
            entered_date = entered_date.replace(i, '-')
    # print(entered_date)
    entered_date_split = entered_date.split('-')
    entered_date_split = entered_date_split[-1:] + entered_date_split[:-1]
    # print(entered_date_split[1])
    # print(entered_date_split[2])
    # print(entered_date_split[0])
    entered_date = '-'.join(entered_date_split)
    print(entered_date)
    if len(entered_date_split) > 3:
        raise exceptions.OutOfBounds
    elif int(entered_date_split[1]) <= 1 and int(entered_date_split[1]) >= 12:
        raise exceptions.NonValdMonth
    elif int(entered_date_split[2]) <= 1 and int(entered_date_split[2]) >= 31:
        raise exceptions.NotValidDay
    elif int(entered_date[0]) > TODAY.year:
        raise exceptions.NotValidYear
    # elif datetime.datetime.strptime(entered_date, "%y-%m-%d"):
    #     raise exceptions.NotValidDate
    else:
        return entered_date
    # print(entered_date)
    # print(today)
    # print(today.year, today.day, today.month)
    # today_spilt = today.split('-')
    # print(today_spilt)
    # print(today)
    # print(split.split())


def introStatement():
    print("Welcome to the Say Yes Project")
    print("Congradulations on your upcoming wedding!")
    print("Lets get some information from you before we create your list!")
    user_name = input("What is your name? ")
    partner_name = input("What is your partner's name? ")
    wedding_date = input(
        "What date are you looking at for your wedding? Please enter in this form (DD/MM/YYYY): ")
    return user_name, partner_name, wedding_date


if __name__ == "__main__":
    # basic_info = introStatement()
    # print(basic_info)  # returns name,  partner, wedding date as a LIST
    #     print(basic_info[2]) # gives me al
    #     date = basic_info[2].split()
    #     # print(date)
    # place = ['27/10/2024']
    # date_valid(place)
    # date_valid(place)
    # place = ['10/24/2024']
    # date_valid(place)
    try:  # TRY BLOCK
        # introStatement()
        place = ['10/24/2024']
        done = False
        while not done:
            #result = introStatement()
            # thee result should be introstatement()
            result = date_valid(place)
            done = True
    except exceptions.OutOfBounds:
        print(
            "You have entered a invalid Date please try again with this format (DD/MM/YYYY)")
    except exceptions.NotValidDate:
        print("You have entered a invalid date please try ")
    except exceptions.NotValidYear:
        print(f"Please enter a date greater than: {TODAY.year}")
    except exceptions.NonValdMonth:
        print("You enterd a month that does not exist please try again")
    except exceptions.NotValidDay:
        print("Please enter a date that is between 1 - 31")
    else:
        # start of the taking in the data
        print(result)
