#!/usr/bin/python3.4

#Exercise: 14.9
#By: Robert A. Walters
#Created on: 2/10/16
#Program Description: A Hangman game

def main():
        print("Lets Play Hangman!")
        choice = eval(input("Press '1' to play or '2' to quit: "))

        if choice == 1:
                print("Lets Play! Good Luck!!")
                print("Please make sure that the letters are LOWER CASE")
                game()
        elif choice == 2:
                print("Maybe next time")
        else:
                print("Please use numbers '1' or '2'")

def game():
        print("You get 9 wrong chances")
        guesses = 1
        letters_used = ""
        word = "coyotes"
        progress = ["?","?","?","?","?","?","?"]

        while guesses < 9:
                guess = input("Guess a letter: ")
                if guess in word not in letters_used:
                        letters_used += "  " + guess
                        hangman(guesses)
                        progress_update(progress, word, guess)
                        print("Good Guess!")
                        print("Progress: " + progress_update(guess, word, progress))
                        print("Letters used: " + letters_used)
                        win(progress)
                elif guess not in word not in letters_used:
                        guesses +=1
                        letters_used += "," + guess
                        hangman(guesses)
                        print("Wrong!")
                        progress_update(progress, word, guess)
                        print("Progress: " + "".join(progress))
                        print("Letters used: " + letters_used)
                        win(progress)
                else:
                        print("Please enter a valid character")
def win(progress):
        win = int(0)
        for x in progress:
                if (x != '?'):
                        win += 1
                if win == len(progress):
                        print("You won go yotes!")
                        exit()
def progress_update(guess, word, progress):
        i = 0
        while i < len(word):
                if guess == word[i]:
                        progress[i] = guess
                        i += 1
                else:
                        i += 1
        return "".join(progress)
def hangman(guesses):
        if guesses == 1:
                print("___________   ")
                print("|         |   ")
                print("|             ")
                print("|             ")
                print("|             ")
                print("|             ")
                print("              ")
        elif guesses ==2:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|             ")
                print("|             ")
                print("|             ")
                print("|             ")
        elif guesses == 3:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|         '   ")
                print("|             ")
                print("|             ")
                print("|             ")
        elif guesses == 4:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|         '   ")
                print("|        (    ")
                print("|             ")
                print("|             ")
        elif guesses == 5:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|         '   ")
                print("|        ( )  ")
                print("|             ")
                print("|             ")
        elif guesses == 6:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|         '   ")
                print("|       /( )  ")
                print("|             ")
                print("|             ")
        elif guesses == 7:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|         '   ")
                print("|       /( )\ ")
                print("|             ")
                print("|             ")
        elif guesses == 8:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|         '   ")
                print("|       /( )\ ")
                print("|        /    ")
                print("|             ")
        elif guesses == 9:
                print("___________   ")
                print("|         |   ")
                print("|         O   ")
                print("|         '   ")
                print("|       /( )\ ")
                print("|        / \  ")
                print("|             ")
                print("Game Over!!")


main()
#Thanks to kyle car for help me out especially with the hangman ACII art
