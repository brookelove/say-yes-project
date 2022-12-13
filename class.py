# class OutOfBounds (Exception):
#     pass
class UserInfo:
    # def __init__(self, user_name, part_name, location, date:
    #     self.__name = user_name
    #     seld.
    def __init__(self, user_name, partner, location, date):
        # need to have two private and public
        self.__user_name = user_name
        self.__partner = partner
        self.location = location
        self.date = date
        
    def get_info(self):
        return(self.__user_name, self.__partner, self.location, self.date)
    
    