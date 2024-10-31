K = 10  # Set number of wrong guesses allowed to 10

hidden_word = '______'
magic_word = 'PYTHON'

while K > 0 and hidden_word != magic_word: # Terminates when either statement is flase
    print(hidden_word)
    guess = input("Guess a letter: ")
    
    found = False  # To track if the guessed letter was found in magic_word

    # Loops through magic word and checks if user guess is contained within it. If it is, then hidden_word is edited
    for i in range(len(magic_word)):
        if guess.upper() == magic_word[i]:
            hidden_word = hidden_word[:i] + guess.upper() + hidden_word[i + 1:]
            found = True

    if not found:
        K -= 1
        print(f"Wrong guess! Remaining attempts: {K}")

if hidden_word == magic_word:
    print(f"Congratulations! You guessed the word: {hidden_word}")
else:
    print(f"Sorry, you ran out of attempts. The word was: {magic_word}")
