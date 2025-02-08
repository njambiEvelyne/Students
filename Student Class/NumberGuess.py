import random
import emoji

secrect_number = random.randint(0, 3)

try:
    while True:
        guess = int(input("Enter the secret number: "))
        if guess == secrect_number:
            print(emoji.emojize("You won! :party_popper:"))  # 🎉             
            break
        
        else:
            print(emoji.emojize("Sorry. Try again! :crying_face:"))
        play_again = input("Do you want to play again(yes, no): ")
        if play_again != "yes":
            print("Thanks for playing. Goodbye")
            break
      
except ValueError:
    print("Invalid Input. Enter an integer!")
    
