package westtheater;

import java.time.LocalDate;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;

/**
 * Custom checked exception thrown when the West Theater is full.
 * Message includes the movie date and time.
 */
public class WestTheaterFullException extends Exception {
    private final LocalDate date;
    private final LocalTime time;

    public WestTheaterFullException(LocalDate date, LocalTime time) {
        super();
        this.date = date;
        this.time = time;
    }

    @Override
    public String getMessage() {
        DateTimeFormatter df = DateTimeFormatter.ISO_DATE;
        DateTimeFormatter tf = DateTimeFormatter.ofPattern("HH:mm");
        return String.format("No Seat Available for %s at %s", date.format(df), time.format(tf));
    }
}
