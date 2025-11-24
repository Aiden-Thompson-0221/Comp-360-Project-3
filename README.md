West Theater Ticket Reservation System

This is a small Python implementation of the West Theater ticket reservation system required for the project.

Features
- WestTheater class with show date/time and capacity (default 200)
- Reserve seats, cancel reservations
- Custom WestTheaterFull exception showing date and time when theater is full

Files
- `exceptions.py` - defines the `WestTheaterFull` exception
- `theater.py` - contains `WestTheater` implementation
- `main.py` - demo runner showing sample usage
- `tests/test_theater.py` - unit tests (run with pytest)

How to run (Windows PowerShell)

# Run demo
python main.py

# Run tests (requires pytest)
python -m pytest -q

Notes
- Rows are 1..10 and columns 1..20.
- When the theater is full, reserving raises `WestTheaterFull`, message contains date and time.
