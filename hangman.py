import random
def hangman_game():

    # Welcome the user
    name = input("What is your name ?")

    print("Hello, " + name, "It's time to play hangman !!")

    print (" Start guessing....")

    words = ['rainbow', 'computer', 'science', 'programming',
             'python', 'mathematics', 'player', 'condition',
             'reverse', 'water', 'board', 'life', 'java', 'family', 'dark','Table']
    word = random.choice(words)
    #determine the number of turns
    turns = 10

    # creates a variable with an empty value
    guesses = " "

    # saving the word to be guessed


    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed +=1
        if failed == 0:
            print("Congrats!! You Won!!")
            break

        #taking the guess inour from the user
        guess = input("Guess a charater...")
        guesses += guess
        if guess not in word:
            turns -= 1
            print("Wrong guess :( ")
        print("You have", +turns, "more guesses")

        if turns == 0:
            print("Game over, you lost")

    check = input("Do you want to play again Y/N ?")
    if check == "Y":
        hangman_game()

hangman_game()
