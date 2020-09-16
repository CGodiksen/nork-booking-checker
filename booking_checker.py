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
        self.bookings = self.booking_scraper

        self.__extract_bookings("https://www.conventus.dk/dataudv/www/booking.php?idv1=1&idv2=06:00&idv3=23:30&idv4=201"
                                "21&idv5=10126&d=20&m=09&y=20&navn=skjul&ressourceliste=skjul&banebooking=skjul&login_"
                                "boks=vis&handelsbetingelser=vis&engine_error=&alt_farver=skjul")


test = BookingChecker("test")
