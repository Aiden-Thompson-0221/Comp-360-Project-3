from theater import WestTheater
from exceptions import WestTheaterFull


def demo():
    # sample run that demonstrates reservation, full exception and cancellation
    theater = WestTheater(date="2025-12-01", time="19:30")

    print(theater.show_info())

    # Reserve a few seats
    for i in range(3):
        row, col = theater.reserve_seat()
        print(f"Reserved seat for {theater.date} at {theater.time}: Row {row}, Column {col}")

    # Fill up the remaining seats quickly (but not printing each)
    try:
        while True:
            theater.reserve_seat()
    except WestTheaterFull as e:
        print(str(e))

    print(theater.show_info())

    # Cancel one seat and reserve again
    cancelled = theater.cancel_seat(1, 1)
    print("Cancelled seat (1,1):", cancelled)
    try:
        row, col = theater.reserve_seat()
        print(f"Reserved seat after cancellation for {theater.date} at {theater.time}: Row {row}, Column {col}")
    except WestTheaterFull as e:
        print(str(e))


if __name__ == "__main__":
    demo()
