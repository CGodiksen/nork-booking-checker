import requests
from bs4 import BeautifulSoup


class BookingChecker:
    """
    Class providing methods for scraping the NORK fitness booking site and checking for double bookings.
    """
    def __init__(self, name):
        """
        :param name: The name of the person who is checked for double bookings.
        """
        self.name = name

        # List of bookings, each booking represented by a tuple with the format (time_interval, name).
        self.bookings = []

        self.__extract_bookings("https://www.conventus.dk/dataudv/www/booking.php?idv1=1&idv2=06:00&idv3=23:30&idv4=201"
                                "21&idv5=10126&d=20&m=09&y=20&navn=skjul&ressourceliste=skjul&banebooking=skjul&login_"
                                "boks=vis&handelsbetingelser=vis&engine_error=&alt_farver=skjul")

    def update_bookings(self):
        """
        Scrapes two weeks of data from each of the four booking sites for the fitness room and updates the bookings.
        """

    def __extract_bookings(self, url):
        """
        Gets the HTML from the given URL and extracts the bookings from the code.

        :param url: The URL of the website containing the table that shows bookings for one week.
        :return: A list of all bookings from the booking table.
        """
        bookings = []

        request = requests.get(url)
        html = request.text

        soup = BeautifulSoup(html, "html.parser")

        # Iterating through each "day" column in the booking table by searching for the specific html attributes.
        for count, day in enumerate(soup.find_all("td", attrs={"class": "noPad", "width": "14%", "valign": "top",
                                                               "bgcolor": "#E1E1E1", "align": "left"})):
            for booking in day.find_all("td", attrs={"style": "background-color: #F6B448 !important;"}):
                print(count + 1, booking.attrs["title"])


test = BookingChecker("test")
