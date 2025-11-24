from typing import Optional, Tuple
from exceptions import WestTheaterFull


class WestTheater:
    """Represents the West Theater seating and reservation system.

    Seats arranged in 10 rows and 20 columns (rows 1-10, cols 1-20).

    Contract:
    - Constructor(date: str, time: str, num_seats: int) sets up show info.
    - reserve_seat() reserves the next available seat and returns (row,col).
    - cancel_seat(row,col) frees up a reserved seat.
    - is_full() -> bool checks if all seats reserved.

    Error modes:
    - WestTheaterFull thrown on attempt to reserve when full.
    """

    ROWS = 10
    COLS = 20
    TOTAL = ROWS * COLS

    def __init__(self, date: str, time: str, num_seats: Optional[int] = None):
        # number of seats for the show (default to theater capacity)
        self.date = date
        self.time = time
        self.capacity = num_seats if num_seats is not None else WestTheater.TOTAL
        if self.capacity > WestTheater.TOTAL:
            raise ValueError("Capacity cannot exceed theater total seats")

        # seats: False = available, True = reserved
        # Use 1-based indexing for display; store 0-based internally
        self._seats = [[False for _ in range(WestTheater.COLS)] for _ in range(WestTheater.ROWS)]
        self._reserved_count = 0

    def is_full(self) -> bool:
        return self._reserved_count >= self.capacity

    def _find_next_available(self) -> Optional[Tuple[int, int]]:
        if self.is_full():
            return None
        for r in range(WestTheater.ROWS):
            for c in range(WestTheater.COLS):
                if not self._seats[r][c]:
                    # ensure we don't exceed configured capacity (partial fill)
                    # we treat capacity as the maximum allowed reserved seats, not specific seat masking
                    return (r, c)
        return None

    def reserve_seat(self) -> Tuple[int, int]:
        """Reserves the next available seat and returns (row, col) 1-based.

        Raises WestTheaterFull with date/time when no seats available.
        """
        if self.is_full():
            raise WestTheaterFull(self.date, self.time)

        coord = self._find_next_available()
        if coord is None:
            # double-check
            raise WestTheaterFull(self.date, self.time)

        r, c = coord
        self._seats[r][c] = True
        self._reserved_count += 1
        # Return 1-based indices
        return (r + 1, c + 1)

    def cancel_seat(self, row: int, col: int) -> bool:
        """Cancel reservation for given 1-based (row, col).

        Returns True if cancellation succeeded, False if seat was not reserved or invalid.
        """
        if not (1 <= row <= WestTheater.ROWS and 1 <= col <= WestTheater.COLS):
            return False
        r = row - 1
        c = col - 1
        if not self._seats[r][c]:
            return False
        self._seats[r][c] = False
        self._reserved_count -= 1
        return True

    def seat_status(self, row: int, col: int) -> Optional[bool]:
        """Return True if reserved, False if available, None if invalid."""
        if not (1 <= row <= WestTheater.ROWS and 1 <= col <= WestTheater.COLS):
            return None
        return self._seats[row - 1][col - 1]

    def reserved_count(self) -> int:
        return self._reserved_count

    def show_info(self) -> str:
        return f"Date: {self.date}, Time: {self.time}, Reserved: {self._reserved_count}/{self.capacity}"
