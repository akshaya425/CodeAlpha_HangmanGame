import random

words = ["python", "laptop", "coding", "college", "program"]

secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect attempts.")

while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word!")
        break

    guess = input("Enter a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Attempts remaining:", attempts)

else:
    print("\n😢 Game over! The word was:", secret_word)