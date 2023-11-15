# A program that roles one die before asking for any input is boring and not useful
# Make a program that gets the number of dice to roll before rolling.
# Set dice at D6, meaning 6 sides.

from random import randrange
from random import randint

# Tracks if user wants to roll_again (or program initialized)
roll_again = True

# While user wants to roll again (or first time executing program)
while True:

    # Prompt for how many dice to roll
    roll_prompt = input('How many dice do you want me to roll? ')
    dice_to_roll = int(roll_prompt)

    # Setup data structure to hold results
    roll_result = []

    # Roll dice input amount of times and store results in data structure
    # TURN THIS INTO A COMPREHENSION
    for roll in range(0, dice_to_roll):

        # Generate random number for roll of D6 die
        #num_seed = randrange(1, 6)
        num_seed = randint(1, 6)
        roll_result.append(num_seed)


    # Display rolled dice to the user
    print(f'Rolls: {dice_to_roll}\nResult: {roll_result}')

    # Prompt to play again
    # Can restrict input to enums?
    play_again = input('Want to throw again? Y/N')






