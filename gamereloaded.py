import random as r
print("Enter your name:")
name = str(input())
print("=============Welcome " + name + ", to guess the number game. Am thinking of a number between 1 and 10========================")
print("-----------------------------------------------------------------------------------------------------------------------------")
def game_error_checker():#This fuction helps to check the game for errors
    try:
        game_engine()#this is where the game engine was called for the error checking

    except ValueError as  err:
        print(err)
        game_error_checker()
        print("Invalid Input")     
        print("Would you like to continue "+ name)
        print("type Y for yes or N for No")
        print("Please " + name +  " Kindly input integers only, between 1 & 10")
        play_again_func()
def play_again_func():# this function helps the player to play the game again
    play_again = str(input())
    play_again = play_again.upper()
    if play_again == "Y":
        game_engine()
    elif play_again == "N":
        print("*******Thanks For Playing," + name + " Goodbye******")
        exit()
def game_engine():#This is the main game engine
    
    num = r.randint(1,10)
    try:
        for i in range(1,10):
            print("********KINDLY TAKE A GUESS********")

            player_guess = int(input())

            if player_guess > num:
                print("C'mon that's too high, guess lower")
            elif player_guess < num:
                print("Hey that's too low, guess higer")
            elif player_guess == num:
                print("Good Job, " + name + "! You guessed my number in " + str(i) + " guesses!")
                print("would you like to play again?")
                print("press Y for yes or N for No")
                play_again_func()
        else:
            print(">>>>>^^^GAME OVER^^^<<<<<<<<")
            print("Oh, sorry the number i was thinking of was " +str(num))
            print("Dont feel bad try harder next time.")
            print("press Y for yes or N for No")
            play_again_func()
    except ValueError:
        print("Invalid input")
        print("Would you like to continue "+ name)
        print("type Y for yes or N for No")
        print("Please " + name +  " Kindly input integers only, between 1 & 10")

        play_again_func()
        
game_engine()
