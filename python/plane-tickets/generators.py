"""Functions to automate Conda airlines ticketing system.

    In this iteration I'm playing around with returning
    generator *expressions*, as opposed to using yield within
    the functions.
    """


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    """

    return ('ABCD'[seat % 4] for seat in range(number))


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    """

    seats = range(number + 4 if number >= 13 else number)
    letters = generate_seat_letters(number)

    return (f'{str(row)}{next(letters)}' for
            seat in seats if (row := seat // 4 + 1) != 13)


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list containing names of passengers.
    :return: dict - with keys = passenger names and values = seat numbers.

    """

    return {passenger: seat for passenger, seat in
            zip(passengers, generate_seats(len(passengers)))}


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    return (base.ljust(12, '0') for
            seat in seat_numbers if
            (base := f'{seat}{flight_id}'))
