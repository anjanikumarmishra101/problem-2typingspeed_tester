
import time
import random
import string

def test_typing_speed():
    # Generate a random string of 100 characters
    random_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(100))

    # Display the random string to the user
    print("Type the following string:")
    print(random_string)

    # Start the timer
    start_time = time.time()

    # Get the user's input
    user_input = input()

    # Stop the timer
    end_time = time.time()

    # Calculate the time taken to type the string
    time_taken = end_time - start_time

    # Check if the user's input matches the random string
    if user_input == random_string:
        print(f"Correct! Your typing speed is {len(random_string) / time_taken} characters per second.")
    else:
        print("Incorrect. Please try again.")

# Run the typing speed test
test_typing_speed()