import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___
     /___\\
     (o o)
     ( : )
     ( : )
    """,
    # Stage 1: Bottom part starts melting
    """
      ___
     /___\\
     (o o)
     ( : )
    """,
    # Stage 2: Only the head remains
    """
      ___
     /___\\
     (o o)
    """,
    # Stage 3: Snowman completely melted
    """
      ___
     /___\\
    """
]


def get_random_word():
    """Select a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current game state."""

    print(STAGES[mistakes])

    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()


def game_loop(secret_word):
    """Run the main game loop."""

    guessed_letters = []
    mistakes = 0

    while True:
        display_game_state(
            mistakes,
            secret_word,
            guessed_letters
        )

        guess = input("Guess a letter: ").lower()
        guessed_letters.append(guess)

        print("You guessed:", guess)


def play_game():
    """Start the game."""

    secret_word = get_random_word()

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)

    game_loop(secret_word)


if __name__ == "__main__":
    play_game()
