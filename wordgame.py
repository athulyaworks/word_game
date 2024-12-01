word = list(input('Enter a word: '))
n = ['_' for letter in word]
print(n)

a = len(word)
guessed_letters = []  # List to track guessed letters

for j in range(a + 2):
    guess = input('Guess a letter: ')
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue  # Skip the rest of the loop and ask for another guess

    guessed_letters.append(guess)  # Add the guessed letter to the list

    if guess in list(word):
        for i in range(a):
            if word[i] == guess:
                n[i] = guess
        print(n)
        print('Guess is correct')
    else:
        print('Wrong letter guessed, try again')

    # Check if the word is completely guessed
    if n == word:
        print('You won the game!')
        break
else:
    print('You lost the game')
