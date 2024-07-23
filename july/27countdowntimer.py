import time
import sys

sec = int(input("Enter time in seconds: "))

for i in range(sec, -1, -1):
    second = i % 60
    minute = (i // 60) % 60
    hour = i // 3600

    # Create the formatted string
    timer = f"{hour:02}:{minute:02}:{second:02}"

    # Print the timer with carriage return to overwrite the previous line
    sys.stdout.write(f"\r{timer}")
    sys.stdout.flush()

    # Wait for 1 second before updating the timer
    time.sleep(1)

# Print a new line after the timer is done
print()