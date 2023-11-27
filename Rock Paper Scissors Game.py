import random
def get_user_input():
    user_choice=input("Select any one of rock,paper,scissors:").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice
def get_computer_input():
    return random.choice(['rock','paper','scissors'])
def determine_the_winner(user_choice, computer_choice):
    if(user_choice==computer_choice):
        return(" The game is tie")
    else:
         if((user_choice=='rock'and computer_choice=='scissors')or
            (user_choice=='paper')and(computer_choice=='rock')or
            (user_choice=='scissors')and(computer_choice=='paper')):
             return ("You Wins!")
         else:
             return ("Computer Wins!")
def play_game():
   user_choice=get_user_input()
   computer_choice=get_computer_input()
   print(f"you chose: {user_choice}")
   print(f"computer chose:{computer_choice}")
   result=determine_the_winner(user_choice,computer_choice)
   print(result)
if __name__== "__main__":
    play_game()
    
