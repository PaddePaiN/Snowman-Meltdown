import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    def game_loop():
        """Main game loop."""

        secret_word = "python"
        guessed_letters = []
        mistakes = 0

        while True:
            print("\nCurrent word:")

            for letter in secret_word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")

            print()

            print(f"Mistakes: {mistakes}")
            print(f"Guessed letters: {guessed_letters}")

            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("Correct!")
            else:
                print("Wrong!")
                mistakes += 1

            """Check win"""
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\nYou won! The word was: {secret_word}")
                break

            """Check loss"""
            if mistakes >= 3:
                print("\nGame over!")
                print(f"The word was: {secret_word}")
                break

    # For now, simply prompt the user once:
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()
