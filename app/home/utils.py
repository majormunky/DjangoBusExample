from . import models


def get_seats_per_row(bus_data):
    """
    This function takes the seat configuration setting, and splits the
    string (ex: 2x3) turns into ["2", "3"].  We then return the value
    of adding both of those items.  This should now return the correct
    value for whatever seat config is setup.
    """
    seat_config = bus_data.seat_configuration
    seat_parts = seat_config.split("x")
    return int(seat_parts[0]) + int(seat_parts[1])


def get_row_configuration(bus_data):
    """
    This looks at the seat config and returns a list where True means
    there is a seat there, and False means its an aisle
    (2x3) -> [True, True, False, True, True, True]
    """

    seat_config = bus_data.seat_configuration
    seat_parts = seat_config.split("x")
    result = []

    for left_seats in range(int(seat_parts[0])):
        result.append(True)
    result.append(False)

    for right_seats in range(int(seat_parts[1])):
        result.append(True)

    return result


def add_seats_for_bus(bus_data):
    # get total seats per row
    seat_config = get_row_configuration(bus_data)

    seats_per_row = seat_config.count(True)
    seat_num = 1

    for seat_row in range(bus_data.row_count):
        for seat_index in range(len(seat_config)):
            if seat_config[seat_index]:
                # this is a seat
                new_seat = models.Seat(
                    bus=bus_data,
                    column=seat_num,
                    row=seat_row + 1
                )
                new_seat.save()
                print("Added Seat:", new_seat)
                seat_num += 1
                print("Incremented Seat Num, now at: ", seat_num)
                if seat_num > seats_per_row:
                    seat_num = 1
                    print("Seat num is larger than seats per row, resetting to 1")
            else:
                # this is an aisle, we can skip it
                print("Found an aisle, skipping.  Seat num is currently", seat_num)
                continue


def organize_seats_for_bus(bus, seats):
    result = []

    # Create a new empty list for each row in our bus
    for _ in range(bus.row_count):
        result.append([])

    # get a list that shows what are seats vs an aisle
    # this will be a list of True = Seat, False = Aisle
    seat_config = get_row_configuration(bus)

    # counters to keep track of where we are at in our loop
    items_in_row = len(seat_config)
    seat_count = 0
    row = 0
    seat_index = 0
    total_seats = len(seats)

    # start building our data structure
    while True:
        # check to see if this loop is for a seat or aisle
        seat_status = seat_config[seat_count]

        if seat_status:
            # this is a seat
            # get our seat from our full seat list
            seat = seats[seat_index]

            # add it to our result in the right row
            result[row].append(seat)

            # add to our seat index to be sure we get
            # the right seat the next loop
            seat_index += 1
        else:
            # this is an aisle
            result[row].append(None)

        # we've created either an aisle or set, increment
        # our seat count
        seat_count += 1

        # now check if our seat count equals how many things
        # we have in a row
        if seat_count == items_in_row:
            # if so, we're done with this row, increment row
            row += 1
            # reset seat counter
            seat_count = 0

        # now check to see if we're done or not
        if seat_index == total_seats:
            # we are, break out of while loop
            break

    return result


def create_bus_seats_for_trip(bus, trip):
    seats = models.Seat.objects.filter(bus=bus)
    for seat in seats:
        seat_link = models.SeatUserLink(
            seat=seat,
            departure_time=trip
        )
        seat_link.save()
