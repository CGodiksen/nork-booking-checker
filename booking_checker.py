from bs4 import BeautifulSoup


class BookingChecker:
    """
    Class providing methods for scraping the NORK fitness booking site and checking for double bookings.
    """
    def __init__(self, name: str, days_ahead: int):
        """
        :param name: The name of the person who is checked for double bookings.
        :param days_ahead: Number specifying how many days ahead the bookings should be checked.
        """
        self.name = name
        self.days_ahead = days_ahead

        # List of bookings, each booking represented by a tuple with the format (time_interval, name).
        self.bookings = None

    def update_bookings(self):
        """
        Scrapes the four booking sites for the fitness room and gets the bookings for the specified
        number of days ahead.
        """
