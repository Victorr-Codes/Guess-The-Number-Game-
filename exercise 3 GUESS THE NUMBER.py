print("WELCOME TO 'GUESSING THE NUMBER' GAME")
n = 18
no_of_times = 1
print("Number of guesses is limited to only 9 times")

while(no_of_times<=9):
    user = int(input("Guess the number\n"))
    if user<n:
        print("you entered a lesser number please input a greater number.\n")
        
    elif user>n:
        print("you entered greater number please input a smaller number.\n")
        
    else:
        print("You won\n")
        print(no_of_times , "number of guesses you took to finish.")
        break
    print(9-no_of_times,"no. of guesses left")
    no_of_times = no_of_times + 1

if(no_of_times>9):
    print("Game over")
    print("The number was 18")



