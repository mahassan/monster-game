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
#first_name = input('Enter your name? ')
ask_name = "Enter your name?"
def typewriter(write):
    for char in write:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

typewriter(ask_name)
name = input()
def final_choice_of_the_user() :
    decision = input("Do you want to play again (enter yes or no) ").lower()
    while(decision != "yes" and decision != "no") :
        decision = input("      either 'yes' or 'no' please      ").lower()
        if decision == 'yes' :
            start_game()
            break
        elif decision == 'no' :
            game_start_end_creditrs.game_over_ascii(name)

def start_game():
    typewriter(f'Welcome, {name}: You are walking along and you come across a friendly looking monster \n')
    jungle.hello_from_monster_ascii()

    typewriter('Monster, do you need any help? \n')
    typewriter('Enter Option yes or no \n')

    selection = input()

    if selection == 'no'.lower():
        typewriter("You Declined Monster's help.\n")
        typewriter("Ok, but be careful in the forest.")
        typewriter("You go alone. Walking in deep forest.")

        jungle.going_alone_ascii()

        typewriter("You fall down a pit.\n")
        
        jungle.snake_ascii()

        game_start_end_creditrs.game_over_ascii(name)

        final_choice_of_the_user()
    
start_game()