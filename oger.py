import sys, time, os
import jungle
import game_start_end_creditrs
#ASCII for game start
print(""" 
 __  __                 _               _____                      
|  \/  |               | |             / ____|                     
| \  / | ___  _ __  ___| |_ ___ _ __  | |  __  __ _ _ __ ___   ___ 
| |\/| |/ _ \| '_ \/ __| __/ _ \ '__| | | |_ |/ _` | '_ ` _ \ / _ \
| |  | | (_) | | | \__ \ ||  __/ |    | |__| | (_| | | | | | |  __/
|_|  |_|\___/|_| |_|___/\__\___|_|     \_____|\__,_|_| |_| |_|\___|

""")
first_name = input('Enter your name? ')

# Function
# Player went alone ASCII

# def start_again():
#     decision = input("Do you want to play again ")
#     print(decision)
#     while(decision != "yes" ):
#         start_again()
#         decision = True
#     if decision == "yes":
#         start_game()
#     else:
#         game_over()
def final_choice_of_the_user() :
    decision = input("Do you want to play again (enter yes or no) ").lower()
    while(decision != "yes" and decision != "no") :
        decision = input("      either 'yes' or 'no' please      ").lower()
        print(f"fdecision  {decision}")
    if decision == 'yes' :
        start_game()
    elif decision == 'no' :
        game_start_end_creditrs.game_over_ascii(first_name)

def start_game():
    print(f'Welcome, {first_name}: You are walking along and you come across a friendly looking monster \n')

    jungle.hello_from_monster_ascii()

    print('Monster, do you need any help?')

    print('Enter Option yes or no')

    selection = input()

    if selection == 'no'.lower():
        print("You Declined Monster's help\n")

        print("You choose to go alone. Walking in deep forest.")

        jungle.going_alone_ascii()

        print("You fall down a pit and the monster rescues you\n")
        
        jungle.snake_ascii()

        print('Go in the forest alone, a snake bit suddenly and you die')

        game_start_end_creditrs.game_over_ascii(first_name)

        final_choice_of_the_user()
    

start_game()