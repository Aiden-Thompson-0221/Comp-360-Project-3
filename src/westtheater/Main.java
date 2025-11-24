package westtheater;

import java.time.LocalDate;
import java.time.LocalTime;

/**
 * Simple demo for the WestTheater reservation system.
 * It fills the theater, then attempts one more reservation to trigger the custom exception.
 */
public class Main {
    public static void main(String[] args) {
        LocalDate movieDate = LocalDate.of(2025, 12, 25);
        LocalTime movieTime = LocalTime.of(19, 30);

        WestTheater theater = new WestTheater(movieDate, movieTime);

        try {
            // Reserve every seat
            for (int r = 1; r <= WestTheater.ROWS; r++) {
                for (int c = 1; c <= WestTheater.COLS; c++) {
                    theater.reserveSeat(r, c);
                }
            }

            System.out.println("All seats reserved. Trying one more reservation to show the exception...");

            // Attempt to reserve one more seat (should throw WestTheaterFullException)
            theater.reserveSeat(1, 1);

        } catch (WestTheaterFullException e) {
            // Requirement: display "No Seat Available" information that must include date and time.
            System.out.println(e.getMessage());
        } catch (IllegalStateException | IllegalArgumentException e) {
            System.out.println("Reservation error: " + e.getMessage());
        }

        // Demonstrate cancellation and re-reservation
        System.out.println("\nCanceling seat (1,1) and reserving it again...");
        theater.cancelReservation(1, 1);
        try {
            theater.reserveSeat(1, 1);
        } catch (WestTheaterFullException e) {
            // If theater was still considered full (shouldn't be after a cancel) print message
            System.out.println(e.getMessage());
        }

        System.out.printf("Available seats now: %d%n", theater.availableSeats());
    }
}
