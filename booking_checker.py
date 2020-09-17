import schedule
from datetime import datetime
from booking_scraper import BookingScraper
from email_sender import EmailSender


class BookingChecker:
    def __init__(self, name):
        """
        :param name: The name of the person who is checked for double bookings.
        """
        self.name = name

        self.booking_scraper = BookingScraper()
        self.email_sender = EmailSender("christian.programming55@gmail.com", "christian.godiksen55@gmail.com")

        # List of bookings, each booking represented by a tuple with the format (time_interval, name).
        self.bookings = None

    def booking_checker_job(self):
        """Method that is called by the scheduler every 15 minutes to provide periodic checks to the booking system."""
        self.bookings = self.booking_scraper.get_bookings()
        self.email_sender.send_conflict_email(self.__check_double_booking())

    def __check_double_booking(self):
        """
        Checks the current bookings for double bookings involving the specified name. A double booking is when the
        fitness room is booked by two people at the same time.

        :return: A list of double bookings involving the specified name. Empty list if no double bookings were found.
        """
        double_bookings = []

        # Creating a list of the bookings made by the specified name that are not in the past.
        name_bookings = [booking for booking in self.bookings
                         if booking["name"] == self.name and booking["end_datetime"] >= datetime.now()]

        # Checking each booking for conflicts that would result in a double booking.
        for name_booking in name_bookings:
            for booking in self.bookings:
                if booking["name"] != self.name:
                    start_conflict = booking["start_datetime"] <= name_booking["start_datetime"] < booking["end_datetime"]
                    end_conflict = booking["start_datetime"] < name_booking["end_datetime"] <= booking["end_datetime"]
                    if start_conflict or end_conflict:
                        double_bookings.append((name_booking, booking))

        return double_bookings
