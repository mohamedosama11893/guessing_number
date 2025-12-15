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
