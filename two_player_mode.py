import os
import sys
from logic import calc_response

NUMBER_OF_DIGITS = 4


def clear_screen():
    """Clear console to hide the secret code."""
    os.system("cls" if os.name == "nt" else "clear")


def get_secret_from_player(player_name):
    """
    Prompt a player to enter a secret code.
    Code is visible while being entered (acceptable per requirements).
    """
    while True:
        try:
            secret_str = input(
                f"{player_name}, enter your secret code ({NUMBER_OF_DIGITS} digits, 0-9): "
            ).strip()
            secret = int(secret_str)
            
            if secret < 0 or secret >= 10**NUMBER_OF_DIGITS:
                print(
                    f"Please enter a number between 0 and {10**NUMBER_OF_DIGITS - 1}"
                )
                continue
            
            return secret
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play_guessing_turn(guesser_name, code_setter_name, secret):
    """
    Run a guessing turn: guesser tries to crack the secret until they succeed or quit.
    Returns the number of guesses taken (lower is better), or None if player quits.
    """
    max_val = 10**NUMBER_OF_DIGITS
    guess_count = 0
    guess = max_val  # Initial value different from any valid secret
    
    print(f"\n{guesser_name}, try to crack {code_setter_name}'s code!\n")
    
    while guess != secret:
        guess_count += 1
        raw_input = input(f"Guess #{guess_count} (0-{max_val - 1}, or 'h' for help, 'q' to quit): ").strip()
        
        if raw_input.lower() == "q":
            print(f"{guesser_name} quit. Game over!")
            return None
        
        if raw_input.lower() == "h":
            print("Enter a 4-digit number to guess. Get '*' for correct digit in correct position,")
            print("'+' for correct digit in wrong position.")
            continue
        
        try:
            guess = int(raw_input)
            if guess < 0 or guess >= max_val:
                print(f"Please enter a number between 0 and {max_val - 1}")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number or 'h' for help.")
            continue
        
        response = calc_response(secret, guess, NUMBER_OF_DIGITS)
        format_str = f"{{guess:0{NUMBER_OF_DIGITS}}} {{response:{NUMBER_OF_DIGITS}}}"
        print(format_str.format(guess=guess, response=response))
    
    print(f"\n✓ {guesser_name} cracked the code in {guess_count} guesses!")
    return guess_count


def play_two_player_match():
    """
    Run an infinite two-player Mastermind game.
    Each round: Player 1 sets code → Player 2 guesses once → Player 1 guesses once.
    At the end of each round, players decide to continue or stop.
    Track scores (win count) across rounds.
    """
    print("\n" + "="*60)
    print("WELCOME TO TWO-PLAYER MASTERMIND!")
    print("="*60)
    
    # Get player names
    player1 = input("Player 1 name: ").strip() or "Player 1"
    player2 = input("Player 2 name: ").strip() or "Player 2"
    
    total_guesses = {player1: 0, player2: 0}
    players = [player1, player2]
    round_num = 0
    
    game_running = True
    while game_running:
        round_num += 1
        print(f"\n{'#'*60}")
        print(f"ROUND {round_num}")
        print(f"{'#'*60}\n")
        
        # Player 1 sets a secret, Player 2 guesses once
        print(f"{player1} sets a secret code for {player2} to guess.")
        secret1 = get_secret_from_player(player1)
        clear_screen()
        
        guesses1 = play_guessing_turn(player2, player1, secret1)
        
        if guesses1 is None:
            # Player quit
            print(f"\nGame ended by {player2}.")
            game_running = False
            break
        else:
            # Player 2 cracked the code
            total_guesses[player2] += guesses1
        
        # Player 2 sets a secret, Player 1 guesses once
        print(f"\n{'-'*60}")
        print(f"{player2} sets a secret code for {player1} to guess.")
        secret2 = get_secret_from_player(player2)
        clear_screen()
        
        guesses2 = play_guessing_turn(player1, player2, secret2)
        
        if guesses2 is None:
            # Player quit
            print(f"\nGame ended by {player1}.")
            game_running = False
            break
        else:
            # Player 1 cracked the code
            total_guesses[player1] += guesses2
        
        # Display round results
        print(f"\n{'-'*60}")
        print(f"ROUND {round_num} RESULTS:")
        for player in players:
            print(f"  {player}: {total_guesses[player]} total guesses")
        print(f"{'-'*60}\n")
        
        # Ask if players want to continue
        continue_choice = input("Play another round? (y/n): ").strip().lower()
        if continue_choice != "y":
            game_running = False
    
    # Final results
    print(f"\n{'#'*60}")
    print("GAME OVER!")
    print(f"{'#'*60}")
    print("\nFINAL SCORES:")
    for player in players:
        print(f"  {player}: {total_guesses[player]} total guesses")
    
    # Determine winner (fewest guesses)
    min_guesses = min(total_guesses.values())
    winners = [p for p in players if total_guesses[p] == min_guesses]
    
    if len(winners) == 1:
        print(f"\n🏆 {winners[0]} WINS! 🏆")
    else:
        print(f"\n🏆 TIE! 🏆")


if __name__ == "__main__":
    try:
        play_two_player_match()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")
        sys.exit(0)
