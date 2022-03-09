

word = input("please input a 5 letter word--")

listed_word = list(word)
print(listed_word)

guessing = True
guess_count = 0
while guessing:
    player_guess = input("Please input a guess--")
    listed_guess = list(player_guess)
    print(listed_guess)
    guess_count += 1

    for i in range(len(listed_word)):
        listed_word = listed_word
        letter = listed_guess[i]
        if letter == listed_word[i]:
            print(letter + " is in correct position " + str(i + 1))
            listed_word[i] = " "
            print(listed_word)
        elif letter in listed_word:
            print(letter, "in word, wrong position")
            listed_word.remove(letter)

    # sort_word = sorted(listed_word)
    # print(sort_word)
    # sort_guess = sorted(listed_guess)
    # print(sort_guess)

    # wordd = set(word)
    # print(wordd)
    # guesss = set(player_guess)
    # common_char = wordd & guesss
    # print(common_char)

    # for i in range(len(player_guess)):
    #     letter = listed_guess[i]
    #     sort_letter = sort_guess[i]
    #
    #     if letter == listed_word[i]:
    #         print(letter + " is in correct position " + str(i + 1))
    #     elif sort_letter in sort_word:
    #         print("in word, wrong position")

    # for position in range(len(player_guess)):
    #     letter = player_guess[position]
    #     if letter == word[position]:
    #         print(letter + " is in correct position " + str(position+1))
    #     elif letter in sort_word:
    #         print("in word, wrong position")

    if listed_guess == listed_word:
        print("Congrats, you completed the wordle in " + str(guess_count) + " attempts")
        guessing = False
    elif guess_count > 4:
        print("you are out of guesses dummy, word was " + word)
        guessing = False