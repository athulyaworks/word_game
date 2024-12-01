word=list(input('Enter a word:'))
n=['_' for letter in word]
print(n)
a=len(word)
for j in range(a+2):
    guess=input('Guess a letter:')
    if guess in list(word):
        for i in range(a):
            if word[i]==guess:
                n[i]=(guess)
                print(n)
                print('guess is correct')
                break
    else:
        print('wrong letter guessed,try again')
if n==word:
    print('You won the game')
else:
    print('You lost')           
                    
        



