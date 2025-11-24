import pytest
from theater import WestTheater
from exceptions import WestTheaterFull


def test_reserve_and_cancel():
    t = WestTheater(date="2025-12-01", time="19:30")
    assert not t.is_full()
    r1 = t.reserve_seat()
    assert isinstance(r1[0], int) and isinstance(r1[1], int)
    assert t.reserved_count() == 1
    # Cancel and check
    assert t.cancel_seat(r1[0], r1[1])
    assert t.reserved_count() == 0


def test_full_raises_exception():
    # create theater with small capacity to test quickly
    t = WestTheater(date="2025-12-02", time="20:00", num_seats=3)
    t.reserve_seat()
    t.reserve_seat()
    t.reserve_seat()
    assert t.is_full()
    with pytest.raises(WestTheaterFull) as exc:
        t.reserve_seat()
    assert "No Seat Available" in str(exc.value) or "No Seat Available" in exc.value.args[0]
    # Check date/time included
    assert "2025-12-02" in str(exc.value)
    assert "20:00" in str(exc.value)


def test_invalid_cancel_returns_false():
    t = WestTheater(date="2025-12-03", time="18:00")
    assert not t.cancel_seat(0, 0)
    assert not t.cancel_seat(11, 1)  # invalid row
    assert not t.cancel_seat(1, 21)  # invalid col

