import random # Generate a random number

number_to_guess = random.randint(1, 100)
# Loop
while True:
    try:
        guess = int(input('Guess the number between 1 ad 100:')) # Loop

        if guess < number_to_guess:
            print('Too low')
        elif guess > number_to_guess:
            print('Too high!')
        else:
            print('Congratulations! You guessed the number.')
            break
    except ValueError:
        print('Please enter a valid number')# Ask the user to make a guess
   
   
    # If not a valid number
    #   Print an error
    # If number < guess
    #   Print too low
    # If number > guess
    #   Print too high
    # Else 
    #   Print well done