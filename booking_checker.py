from booking_scraper import BookingScraper


class BookingChecker:
    """
    Class providing methods for scraping the NORK fitness booking site and checking for double bookings.
    """
    def __init__(self, name):
        """
        :param name: The name of the person who is checked for double bookings.
        """
        self.name = name

        self.booking_scraper = BookingScraper()

        # List of bookings, each booking represented by a tuple with the format (time_interval, name).
        self.bookings = self.booking_scraper.get_bookings()

        print(self.bookings)


test = BookingChecker("test")
