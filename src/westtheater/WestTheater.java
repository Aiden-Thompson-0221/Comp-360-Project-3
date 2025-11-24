package westtheater;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

/**
 * WestTheater represents a 10x20 seating chart (200 seats total).
 * It supports reserving and cancelling seats and throws a
 * WestTheaterFullException when there are no seats available.
 */
public class WestTheater {
    public static final int ROWS = 10;
    public static final int COLS = 20;

    private final LocalDate date;
    private final LocalTime time;
    private final boolean[][] seats; // true == reserved

    public WestTheater(LocalDate date, LocalTime time) {
        this.date = date;
        this.time = time;
        this.seats = new boolean[ROWS][COLS];
    }

    /**
     * Returns true if there are no available seats.
     */
    public boolean WestTheaterFull() {
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (!seats[r][c]) return false;
            }
        }
        return true;
    }

    /**
     * Reserve a specific seat (1-based row and column).
     * If theater is full throws WestTheaterFullException.
     * If the specific seat is already reserved throws IllegalStateException.
     * If row/col out of range throws IllegalArgumentException.
     */
    public void reserveSeat(int row, int col) throws WestTheaterFullException {
        validateRowCol(row, col);

        if (WestTheaterFull()) {
            throw new WestTheaterFullException(date, time);
        }

        int r = row - 1;
        int c = col - 1;
        if (seats[r][c]) {
            throw new IllegalStateException(String.format("Seat (%d,%d) is already reserved.", row, col));
        }

        seats[r][c] = true;
        System.out.printf("Reserved: %s %s - Seat (%d,%d)%n", getDateString(), getTimeString(), row, col);
    }

    /**
     * Cancel a reservation for a specific seat. If the seat was not reserved nothing changes.
     */
    public void cancelReservation(int row, int col) {
        validateRowCol(row, col);
        int r = row - 1;
        int c = col - 1;
        if (!seats[r][c]) {
            System.out.printf("Seat (%d,%d) is not reserved; nothing to cancel.%n", row, col);
            return;
        }
        seats[r][c] = false;
        System.out.printf("Cancelled: %s %s - Seat (%d,%d)%n", getDateString(), getTimeString(), row, col);
    }

    public int availableSeats() {
        int count = 0;
        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (!seats[r][c]) count++;
            }
        }
        return count;
    }

    private void validateRowCol(int row, int col) {
        if (row < 1 || row > ROWS) throw new IllegalArgumentException("Row must be between 1 and " + ROWS);
        if (col < 1 || col > COLS) throw new IllegalArgumentException("Column must be between 1 and " + COLS);
    }

    private String getDateString() {
        DateTimeFormatter df = DateTimeFormatter.ISO_DATE;
        return date.format(df);
    }

    private String getTimeString() {
        DateTimeFormatter tf = DateTimeFormatter.ofPattern("HH:mm");
        return time.format(tf);
    }
}
