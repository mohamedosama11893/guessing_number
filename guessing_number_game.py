"""
Guessing Number Game

This is a console-based number guessing game written in Python.
The game randomly selects a number between 1 and 10, and the player
has up to 3 attempts per round to guess the correct number.

Main Features:
- Input validation to ensure correct numeric and yes/no inputs.
- Provides hints ("Higher" / "Lower") after wrong guesses.
- Tracks total correct guesses, total attempts, and consecutive win streaks.
- Displays a visual progress bar for the win streak.
- The game ends if the player:
  * Wins 5 rounds in a row,
  * Loses a round (fails all 3 attempts),
  * Or chooses to exit voluntarily.

Goal:
Win 5 consecutive rounds to become the champion.

This project demonstrates:
- Functions and modular code design
- Loops and conditional logic
- User input handling and validation
- Basic game state management
"""

import random

# --- Global Variables ---
score = 0              # Total number of correct guesses
total_attempts = 0     # Total number of guesses across all rounds
win_streak = 0         # Number of consecutive round wins

# --- Game Functions ---
def get_yes_no(prompt):
    """
    Ask the player a Yes/No question.

    Keeps looping until the input is either 'yes' or 'no'.

    Args:
        prompt (str): The question displayed to the player.

    Returns:
        str: Either "yes" or "no".
    """
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("yes", "no"):
            return ans
        print("❌ Invalid choice. Please type 'yes' or 'no'.")

#-------------------------------------------------------------------------#

def get_user_guess():
    """
    Ask the player to guess a number between 1 and 10.

    Keeps looping until the user provides a valid integer
    within the range [1, 10].

    Returns:
        int: The valid guess entered by the user.
    """
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if 1 <= guess <= 10:
                return guess
            print("❌ Please enter a number between 1 and 10.")
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            
#==========================================================================#

def progress_bar(streak, max_streak=5, length=10):
    """
    Display a progress bar for the win streak.

    Args:
        streak (int): Current number of consecutive wins.
        max_streak (int, optional): Required streak to win the game. Defaults to 5.
        length (int, optional): Length of the bar in characters. Defaults to 10.

    Returns:
        str: A formatted progress bar string (e.g. [███-------] 3/5).
    """
    progress = min(streak, max_streak) / max_streak
    filled = int(progress * length)
    bar = "█" * filled + "-" * (length - filled)
    return f"[{bar}] {streak}/{max_streak}"

#==============================================================================================================#

def show_status(info):
    """
    Show the current or final game status.

    Args:
        info (dict): Contains game information such as:
            - score (int): Total correct guesses.
            - total_attempts (int): Total guesses across all rounds.
            - win_streak (int): Current consecutive wins.
            - final (bool): Whether to show final status.
            - reason (str): Reason for ending the game.
              Options: "win5", "lost", "exit".
    """
    if info.get("final", False):
        reason = info.get("reason", "exit")

        if reason == "win5":
            # Case: Player won 5 games in a row
            print("🏆🔥 Congratulations! You won 5 games in a row!!")
            print(f"Final score: {info.get('score', 0)}, Total attempts: {info.get('total_attempts', 0)}")
            print("👋 Thanks for playing, you're a champion!")

        elif reason == "lost":
            # Case: Player failed a round
            print("💀 Game Over: You lost the last round.")
            print(f"Final score: {info.get('score', 0)}, Total attempts: {info.get('total_attempts', 0)}")
            if info.get("win_streak", 0) < 5:
                print("🔥 Win Streak Progress:", progress_bar(info.get("win_streak", 0)))
            print("👋 Better luck next time!")

        elif reason == "exit":
            # Case: Player quit voluntarily
            print("👋 You exited the game.")
            if info.get("total_attempts", 0) > 0:
                print(f"Final score: {info.get('score', 0)}, Total attempts: {info.get('total_attempts', 0)}")
                if info.get("win_streak", 0) < 5:
                    print("🔥 Win Streak Progress:", progress_bar(info.get("win_streak", 0)))

    else:
        # Ongoing game status
        print(f"📊 Score so far: {info.get('score', 0)}")
        print("🔥 Win Streak Progress:", progress_bar(info.get("win_streak", 0)))
#==============================================================================================================#

# ---- Main Game Flow ----
print("🎮 Welcome to the Guessing Number Game!")
play_game = get_yes_no("Do you want to play? (yes/no): ")

game_over_reason = "exit"  # Default reason if player quits immediately

while play_game == "yes":
    number = random.randint(1, 10)   # Random target number
    attempts_in_round = 0            # Reset attempts per round
    guessed = False                  # Track if the number was guessed

    # Each round allows up to 3 attempts
    for _ in range(3):
        guess = get_user_guess()
        attempts_in_round += 1
        total_attempts += 1

        if guess == number:
            # Correct guess
            score += 1
            win_streak += 1
            guessed = True
            print("🎉 Correct!")
            show_status({
                "score": score,
                "win_streak": win_streak
            })
            break
        else:
            # Wrong guess → provide hint
            print("⬆️ Higher!" if guess < number else "⬇️ Lower!")

    if not guessed:
        # Player used all 3 attempts → round lost
        print(f"😢 Out of tries! The number was {number}.")
        win_streak = 0
        game_over_reason = "lost"
        break

    # Check if player reached 5 consecutive wins
    if win_streak >= 5:
        game_over_reason = "🎉 5 consecutive wins achieved"
        break

    # Ask if player wants to continue
    play_game = get_yes_no("Play again? (yes/no): ")
    if play_game == "no":
        game_over_reason = "exit"

# Show final game summary
show_status({
    "final": True,
    "reason": game_over_reason,
    "score": score,
    "total_attempts": total_attempts,
    "win_streak": win_streak
})
