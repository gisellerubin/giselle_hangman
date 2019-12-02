import random

ahorcado = ['''
        +---+
        |   |
            |
            |
            |
            |
     =========''', '''


    +---+
    |   |
    O   |
        |
        |
        |
 =========''', '''

      +---+
      |   |
      O   |
      |   |
          |
          |
   =========''', '''

      +---+
      |   |
      O   |
     /|   |
          |
          |
   =========''', '''

      +---+
      |   |
      O   |
     /|\  |
          |
          |
   =========''', '''

      +---+
      |   |
      O   |
     /|\  |
    /     |
          |
   =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

words ='giselle princess queen girl unicorn pink purple gigi gigithequeen '.split()

def random_words(wordlist):
    word_index= random.randint(0, len(wordlist)-1)
    return wordlist[word_index]

def show_hangman(ahorcado, wrong_words, correct_words,secret_word):
    print(ahorcado[len(wrong_words)])
    print()

    print("The wrong words:",end=" " )
    for letter in wrong_words:
        print(letter, end=" ")
    print()

    blank_spaces= '_'*len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_words:
            blank_spaces = blank_spaces[:i] +secret_word[i]+ blank_spaces[i+1:]

    for letter in blank_spaces:
            print(letter,end=" " )
    print()
def try_attempt(letters_attempted):
    while True:
        print ("Guess the letter.")
        attempt = input()
        attempt= attempt.lower()
        if len(attempt) !=1:
            print("Please, introduce a letter:")
        elif attempt in letters_attempted:
            print("You have already tryied that letter, Please introduce another one")

        elif attempt not in "abcdefghijklmnopqrstuvwxyz":
            print("Please insert a letter")
        else:
            return attempt
def try_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('s')

print(" H A N G M A N")
wrong_words= ""
correct_words=""
secret_word=random_words(words)
game_over= False

while True:
    show_hangman(ahorcado,wrong_words,correct_words,secret_word)

    attempt = try_attempt(wrong_words,correct_words)

    if attempt in secret_word:
        correct_words= correct_words+ attempt

        found_all_letters= True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_words:
                found_all_letters = False
                break
        if found_all_letters:
            print ("Yes, The secret word is is:  "+ secret_word)

            game_over = True
        else:
            wrong_words = wrong_words + attempt

        if len(wrong_words) == len(ahorcado)-1:
            show_hangman((ahorcado,wrong_words,correct_words,secret_word))
            print("You have run out of attempts \n After:"+ str(len(wrong_words))+"wrong attempts"+ str(len(correct_words))+"correct attempts, the word was: "+ secret_word)
            game_over = True

        if game_over:
            if try_again():
                wrong_words= ""
                correct_words=""
                game_over= False
                secret_word=random_words(words)
            else:
                break

