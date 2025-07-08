from machine import Pin, PWM
import time

# Define the buzzer pin (check your M5StickC documentation for the correct pin)
buzzer_pin = 2  # Example pin, adjust as needed

# Initialize the buzzer pin as a PWM output
buzzer = PWM(Pin(buzzer_pin), freq=440, duty=0)  # Default to off

def beep(frequency, duration_ms):
    """
    Buzzer function for a single beep.
    
    Args:
        frequency (int): Frequency of the beep in Hz.
        duration_ms (int): Duration of the beep in milliseconds.
    """
    buzzer.freq(frequency)
    buzzer.duty(512)  # Set duty cycle for sound (adjust for desired loudness)
    time.sleep_ms(duration_ms)
    buzzer.duty(0)  # Turn off the buzzer

def main():
    """
    Main function to demonstrate buzzer control.
    """
    try:
      while True:
          # Beep with a specific frequency and duration
          beep(1000, 200)  # Beep at 1000Hz for 200ms
          time.sleep_ms(300)
          beep(500, 100)  # Beep at 500Hz for 100ms
          time.sleep(1)

    except KeyboardInterrupt:
        # Handle Ctrl+C to exit gracefully
        buzzer.duty(0) # Ensure buzzer is off when exiting
        print("Exiting...")

if __name__ == "__main__":
    main()