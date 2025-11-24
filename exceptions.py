class WestTheaterFull(Exception):
    """Raised when attempting to reserve a seat but the theater is full."""

    def __init__(self, date: str, time: str):
        self.date = date
        self.time = time
        super().__init__(f"No Seat Available for {date} at {time}")
