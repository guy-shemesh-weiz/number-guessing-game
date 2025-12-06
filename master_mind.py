import random
from logic import calc_response
from two_player_mode import play_two_player_match


INSTRUCTIONS = """
The computer "thinks" a number with 4 different digits.
The user guesses which digits.
For every digit that matched both in value, and in location the computer gives a *.
For every digit that matches in value, but not in space the computer gives you a +.
The user tries to guess the given number in as few guesses as possible.
"""


MAIN_HELP = """
Master Mind game!
s - start a new game (vs computer)
p - play two-player mode
i - print instructions
h - print this menu
q - quit
"""


GAME_HELP = """
q - resign game
h - print this menu
number - a guess
"""

NUMBER_0F_DIGITS = 4


def run_game(number_of_digits):
    max_val = 10**number_of_digits
    secret = random.randrange(max_val)
    # Initial value that for sure will be different than the computer number
    guess = max_val
    resign = False
    guess_number = 0

    print("\n" + "="*60)
    print("The computer has set a secret code.")
    print("="*60 + "\n")
    
    while guess != secret and not resign:
        guess_number += 1
        raw_in = input(f"Guess #{guess_number} (0-{max_val - 1}, or 'h' for help, 'q' to quit): ").strip()
        
        if raw_in.lower() == "q":
            resign = True
            continue
        
        if raw_in.lower() == "h":
            print("Enter a 4-digit number to guess. Get '*' for correct digit in correct position,")
            print("'+' for correct digit in wrong position.")
            continue
        
        try:
            guess = int(raw_in)
            if guess < 0 or guess >= max_val:
                print(f"Please enter a number between 0 and {max_val - 1}")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number or 'h' for help.")
            continue

        response = calc_response(secret, guess, number_of_digits)
        format_str = f"{{guess:0{number_of_digits}}} {{response:{number_of_digits}}}"
        print(format_str.format(guess=guess, response=response))

    print(f"\n{'-'*60}")
    secret_format = f"{{secret:0{number_of_digits}}}"
    if guess == secret:
        print(f"✓ You cracked the code in {guess_number} guesses!")
        print(f"Secret: {secret_format.format(secret=secret)}")
    else:
        print(f"You resigned after {guess_number} guesses.")
        print(f"Secret was: {secret_format.format(secret=secret)}")
    print(f"{'-'*60}\n")
    
    return guess_number if not resign else None


def main():
    best_score = None
    game_on = True
    print("Welcome to Master Mind!")

    while game_on:
        choice = input("Please enter your input: (h for help)\n>> ").strip()
        new_score = None
        if choice == "s":
            new_score = run_game(NUMBER_0F_DIGITS)
            if new_score is not None:
                if best_score is None or new_score < best_score:
                    best_score = new_score
                    print(f"New best score: {best_score} guesses!")
                else:
                    print(f"Best score remains: {best_score} guesses.")
        elif choice == "p":
            play_two_player_match()
        elif choice == "i":
            print(INSTRUCTIONS)
        elif choice == "h":
            print(MAIN_HELP)
        elif choice == "q":
            print("Thank you for playing Master Mind! Goodbye!")
            game_on = False
            break
        else:
            print("Invalid choice. Please try again.")
            print(MAIN_HELP)


if __name__ == "__main__":
    main()
