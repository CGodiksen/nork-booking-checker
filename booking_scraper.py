import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, time


class BookingScraper:
    def __init__(self):
        # The main url for the booking site used to find the url for each individual fitness room booking site.
        self.booking_url = "http://nork.dk/booking/"

    def get_bookings(self):
        """
        Scrapes two weeks of data from each of the four booking sites for the fitness room and updates the bookings.
        """

    def get_individual_booking_urls(self):
        """
        Scrapes the main booking url to find the individual fitness room booking sites. Two URLs are returned for each
        of the four fitness room booking sites to account for the current week and next week.
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

        # Finding the week and year so it can be used to find the date of each booking.
        date_text = soup.find("span", class_="bt", text=re.compile("Uge")).contents[0]
        week = int(date_text[7:9])
        year = int(date_text[11:-6])

        # Iterating through each "day" column in the booking table by searching for the specific html attributes.
        for count, day in enumerate(soup.find_all("td", attrs={"class": "noPad", "width": "14%", "valign": "top",
                                                               "bgcolor": "#E1E1E1", "align": "left"})):
            for booking in day.find_all("td", attrs={"style": "background-color: #F6B448 !important;"}):
                bookings.append(self.__format_booking(booking.attrs["title"], count + 1, week, year))

    @staticmethod
    def __format_booking(title, day, week, year):
        """
        Formats the given information into a dictionary with the keys [name, start datetime, end datetime].

        :param title: The html title of the table element showing a single booking.
        :param day: The week day number as an integer.
        :param week: The week number as an integer.
        :param year: The year as an integer.
        :return: A dictionary containing the extracted information about the booking.
        """
        name = title[5:-22]
        start_time = title[-12:-7]
        end_time = title[-6:-1]

        start_date_time = datetime.combine(date.fromisocalendar(year=year, week=week, day=day),
                                           time(hour=int(start_time[:2]), minute=int(start_time[-2:])))
        end_date_time = datetime.combine(date.fromisocalendar(year=year, week=week, day=day),
                                         time(hour=int(end_time[:2]), minute=int(end_time[-2:])))

        return {"name": name, "start datetime": start_date_time, "end datetime": end_date_time}