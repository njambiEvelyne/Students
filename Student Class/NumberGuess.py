import random

secrect_number = random.randint(0, 10)

try:
    while True:
        guess = int(input("Enter the secret number: "))
        if guess == secrect_number: 
            print("You won!")
            break
        
        else:
            print("Sorry. Try again!")
        play_again = input("Do you want to play again(yes, no): ")
        if play_again != "yes":
            print("Thanks for playing. Goodbye")
            break
      
except ValueError:
    print("Invalid Input. Enter an integer!")
    
