from . import models

def get_seats_per_row(bus_data):
    total_seats_per_row = None
    if bus_data.seat_configuration == "1x1":
        total_seats_per_row = 2
    else:
        total_seats_per_row = 4
    return total_seats_per_row

def add_seats_for_bus(bus_data):
    # get total seats per row
    # we know this is either 1x1 or 2x2, so we can cheat
    total_seats_per_row = get_seats_per_row(bus_data)

    # get total seat count
    total_seats = total_seats_per_row * bus_data.row_count

    for seat_row in range(bus_data.row_count):
        for seat_column in range(total_seats_per_row):
            new_seat = models.Seat(
                bus=bus_data,
                column=seat_column + 1,
                row=seat_row + 1
            )
            new_seat.save()

def organize_seats_for_bus(bus, seats):
    result = []

    # Create a new empty list for each row in our bus
    for _ in range(bus.row_count):
        result.append([])

    # figure out how many seats we have in a row
    seats_per_row = get_seats_per_row(bus)

    # we can cheat here a bit since we know we have equal
    # amount of seats on each side
    seats_per_side = seats_per_row // 2

    # counters to keep track of where we are at in our loop
    seat_count = 0
    row = 0

    # start building our data structure
    for seat in seats:
        # add seat to the row
        result[row].append(seat)

        # increment our seat counter
        seat_count += 1

        # if our seat counter is equal to the seats per side
        # add in an aisle
        if seat_count == seats_per_side:
            result[row].append(None)

        # else if we have filled out our row, go to the next row
        elif seat_count >= seats_per_row:
            row += 1
            seat_count = 0
    return result


def create_bus_seats_for_trip(bus, trip):
    seats = models.Seat.objects.filter(bus=bus)
    for seat in seats:
        seat_link = models.SeatUserLink(
            seat=seat,
            departure_time=trip
        )
        seat_link.save()
