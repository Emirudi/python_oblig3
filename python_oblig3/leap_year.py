class LeapYear:

    def __init__(self, year) -> None:
        self.year = int(year)

    def is_leap_year(self):
        if self.year % 4000 == 0:
            return False
        elif self.year % 400 == 0:
            return True
        elif (self.year % 4 == 0) and (self.year % 100 != 0):
            return True
        else:
            return False
