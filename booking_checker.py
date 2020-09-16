from datetime import datetime
from booking_scraper import BookingScraper


class BookingChecker:
    def __init__(self, name):
        """
        :param name: The name of the person who is checked for double bookings.
        """
        self.name = name

        self.booking_scraper = BookingScraper()

        # List of bookings, each booking represented by a tuple with the format (time_interval, name).
        self.bookings = self.booking_scraper.get_bookings()

        print(self.bookings)

        print(self.__check_double_booking())

    def __check_double_booking(self):
        """
        Checks the current bookings for double bookings involving the specified name. A double booking is when the
        fitness room is booked by two people at the same time.

        :return: A list of double bookings involving the specified name. Empty list if no double bookings were found.
        """
        double_bookings = []

        # Creating a list of the bookings made by the specified name that are not in the past.
        name_bookings = [booking for booking in self.bookings
                         if booking["name"] == self.name and booking["end datetime"] >= datetime.now()]

        # Checking each booking for conflicts that would result in a double booking.
        for name_booking in name_bookings:
            for booking in self.bookings:
                if booking["name"] != self.name:
                    start_conflict = booking["start datetime"] <= name_booking["start datetime"] < booking["end datetime"]
                    end_conflict = booking["start datetime"] < name_booking["end datetime"] <= booking["end datetime"]
                    if start_conflict or end_conflict:
                        double_bookings.append((name_booking, booking))

        return double_bookings


test = BookingChecker("Christian Godiksen")
