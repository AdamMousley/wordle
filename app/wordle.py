# Wordle game
import string
import random

words_list = ["ahead", "ocean", "smell", "glass", "audio", "crime", "knife", "crane"]
word = random.choice(words_list)
listed_word = list(word)
# word = input("please type a five letter word--")
# listed_word = list(word)
#print(listed_word)
guess_count = 0
guessing = True
alphabet_string = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while guessing:
    print("letters available",alphabet_string)

    player_guess = input("player please input a guess--")
    listed_guess = list(player_guess)
    print(listed_guess)
    guess_count +=1

    if guess_count > 5:
        print("you are out of guesses")
        guessing = False

    for position in range(len(player_guess)):
        letter = player_guess[position]
        if letter == word[position]:
            print(letter, "is in the right place")
        elif letter in word:
            print(letter, "in word, wrong place")
        else:
            if letter in alphabet_string:
                alphabet_string.remove(letter)

    if listed_guess == listed_word:
        print("Congrats, you completed the wordle in " + str(guess_count) + " attempts")
        guessing = False



