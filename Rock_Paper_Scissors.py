import random
def winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
        return "You won the game!"
    else:
        return "Sorry, You have lost the game!"

def rock_paper_scissors():
    user_score,computer_score=0,0
    while True:
        try:
            n=int(input("HOW MANY GAMES DO YOU WANT TO PLAY ? : "))
            if n <= 0:
                print("n should be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
    while n:
        choices = ['rock', 'paper', 'scissors']
        user = input("Enter your choice (rock, paper, or scissors): ").lower()
        while user not in choices:
            print("Invalid choice. Please, Try it again.")
            user = input("Enter your choice (rock, paper, or scissors): ").lower()

        computer = random.choice(choices)
        print(f"The computer chose: {computer}")

        result = winner(user, computer)
        print(result)
        if result=='You won the game!':
            user_score+=1
        elif result=='Sorry, You have lost the game!':
            computer_score+=1
        print("SCORE:")
        print(f"YOUR SCORE :{user_score}    COMPUTER SCORE : {computer_score}")
        n-=1
    return user_score,computer_score
u,c=rock_paper_scissors()
print()
if u > c:
    print("Congratulations!!! You won the game")
elif u < c:
    print("Sorry :( ,You have lost the game")
else:
    print("Hey, It's a Tie")
print()
    
