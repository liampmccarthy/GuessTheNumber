from random import randint

original_smallest_number = smallest_number = 0
original_largest_number = largest_number = 1000
count_no_of_guesses = 0
count_no_of_games = 1

# Pick a secret number
secret_number = randint(original_smallest_number,original_largest_number)

while(True):

    # Work out the guess that is halfway between the smallest and largest number
    halfway = int((smallest_number + largest_number) / 2)


    # Prompt the person to enter a guess between 1 and 100
    print(f"Enter a number between {smallest_number} and {largest_number}. Halfway is {halfway}")

    # Convert guess into a number
    #guess = input()
    guess = halfway
    print(halfway)
    number_guessed = int(guess)
    count_no_of_guesses += 1

    # If number is too low, then tell them to go higher
    if number_guessed < secret_number:
        print("You guessed too low")
        smallest_number = number_guessed + 1
    # If number is too high, then tell them to go lower
    elif number_guessed > secret_number:
        print("You guessed too high")
        largest_number = number_guessed - 1
    # If number is correct, then tell them they won, and exit
    elif number_guessed == secret_number:
        print(f"Well done! You guessed the right number. It took you {count_no_of_guesses} guesses.")
        if count_no_of_guesses < 9:
            print(f"It took {count_no_of_games} to beat the record")
            exit()
        else: 
            count_no_of_guesses = 0
            secret_number = randint(original_smallest_number,original_largest_number)
            smallest_number = original_smallest_number
            largest_number = original_largest_number
            count_no_of_games += 1

               
