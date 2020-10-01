print("WELCOME TO 'GUESSING THE NUMBER' GAME")
print("NOTE-IN THIS GAME YOU HAVE TO GUESS A SECRET NUMBER BY SOME HINTS")
n = 50
no_of_times = 1
var1 = int(input("I how many guesses you can guess the number.\n"))
print("You have",var1,"number of guesses")

while(no_of_times<=var1):
    user = int(input("Guess the number\n"))
    if user<n:
        print("you entered a lesser number please input a greater number.\n")

        
    elif user>n:
        print("you entered greater number please input a smaller number.\n")
        
    else:
        print("You won\n")
        print(no_of_times , "number of guesses you took to finish.")
        break
    print(var1-no_of_times,"number of guesses left")
    no_of_times = no_of_times + 1

if(no_of_times>var1):
    print("Game over")
    print("The number was 18")
