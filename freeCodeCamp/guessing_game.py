secret_word = "python"
guess = ""
counter = 0
limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if counter < limit:
        guess = input("Enter your guess: ").strip().lower()
        counter += 1
    else:
        out_of_guesses = True
        break
if out_of_guesses:
    print("You lose! The secret word was " + secret_word)
else:
    print("You win!")