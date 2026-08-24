import random


def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy   (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard   (1-500, 8 attempts)")

    while True:
        choice = input("Choose 1, 2, or 3: ")

        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 500, 8
        else:
            print("Invalid choice.")


def play_game():
    maximum, max_attempts = choose_difficulty()
    secret_number = random.randint(1, maximum)
    attempts = 0

    print(f"\nI'm thinking of a number between 1 and {maximum}.")
    print(f"You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("\nYour guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > maximum:
            print(f"Choose a number between 1 and {maximum}.")
            continue

        if guess == secret_number:
            score = (max_attempts - attempts + 1) * 100
            print(f"\n🎉 Correct! You got it in {attempts} attempts.")
            print(f"Your score: {score}")
            return

        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        remaining = max_attempts - attempts

        if remaining > 0:
            print(f"Attempts remaining: {remaining}")

    print(f"\nGame over! The number was {secret_number}.")


def main():
    print("===== NUMBER GUESSING GAME =====")

    while True:
        play_game()

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()