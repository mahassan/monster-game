import sys, time, os

def secret_potion():
    print("I see you want to know about the secret potion, Follow me")
def typewriter(message):
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

typewriter(secret_potion)
print("To make the secret potion you will have to get the following riddles correct to collect the accurate ingridients. If you fail to do so the potion will explode 💥")
print("""
    (\
     \ \
 __    \/ ___,.-------..__        __
//\\ _,-'\\               `'--._ //\\
\\ ;'      \\                   `: //
 `(          \\                   )'
   :.          \\,----,         ,;
    `.`--.___   (    /  ___.--','
      `.     ``-----'-''     ,'
         -.               ,-
           `-._______.-'
""")

riddle_1=(input("What must be broken before it can be used?")).lower()
tries=1
while riddle_1 !="egg" and tries <3:
    print("You got the wrong ingridient. You have 3 more chances")
    tries +=1
    print(f"You have made {tries} attempts / 3")
    riddle_1=(input("What must be broken before it can be used?")).lower()

if riddle_1=="egg":
    print("Well Done! You got the first ingridient for the secret potion correct. We need one more ingridient to make the potion")
else:
    print("Your potion has exploded 💥. Game over 💀")

print("""
 (       "     )  APPLYING WHAT I LEARNED   
  ( _  *         FROM THE HARRY POTTER BOOKS
     * (     /      \    ___                
        "     "        _/ /                 
       (   *  )    ___/   |                 
         )   "     _ o)'-./__               
        *  _ )    (_, . $$$                 
        (  )   __ __ 7_ $$$$                
         ( :  { _)  '---  $\                
    ______'___//__\   ____, \               
     )           ( \_/ _____\_              
   .'             \   \------''.            
   |='           '=|  |         )           
   |               |  |  .    _/            
    \    (. ) ,   /  /__I_____\             
snd  '._/_)_(\__.'   (__,(__,_]             
    @---()_.'---@  
""")  
print(input("Do you want to restart the game?Type yes"))
restart_game="yes"
if restart_game=="yes":
    print("restart game")
    #start_game()
else:
    print("Your potion has exploded 💥. Game over 💀")

riddle_2=(input("What vegetable is the most fun to be around and the one everyone wants to hangout with?")).lower()
tries_1=1
while riddle_2 !="fungi" and tries_1 <3:
    print("You got the wrong ingridient. You have 3 more chances")
    tries_1 +=1
    print(f"You have made {tries_1} attempts / 3")
    riddle_2=(input("What vegetable is the most fun to be around and the one everyone wants to hangout with?")).lower()

if riddle_2=="fungi":
    print("Well Done! You got the second ingridient for the secret potion correct.")
else:
    print("Your potion has exploded 💥. Game Over 💀!")
    #start_game()
print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠉⢀⣀⣤⣤⣄⣀⠈⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠋⢀⣴⣾⠿⠛⠛⠛⢛⠿⢿⣶⣤⣀⠉⠒⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⢠⣾⠟⠁⠀⠀⠀⠀⠀⡄⠀⠈⠙⠿⣷⣦⣤⣀⣈⠉⠀⠒⠢⠤⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⣰⣿⢏⠖⠐⠢⡀⠀⠀⠀⠈⠒⠒⠒⠊⠀⠉⠙⠛⠿⠿⣷⣶⣦⣤⣄⠈⠙⠢⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠁⣀⣼⡿⢣⠎⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⢀⠔⠋⠉⠉⠓⢢⡀⠀⢹⠛⣿⢿⣦⡀⠙⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⢠⣾⡿⢋⠜⠁⠀⠀⠀⢀⠏⠀⡴⠚⠙⠒⡄⠀⠈⢦⠀⠀⠀⠀⢀⡇⣰⠃⠀⠀⢥⢻⣷⠀⢹⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠔⠁⢀⣼⡿⡏⠀⢸⡀⠀⠀⢀⡠⠞⠀⠘⣄⠀⠀⢀⠟⠀⠀⠀⠙⠂⠤⠤⣮⠜⠁⣀⡤⠔⠯⢿⢿⠀⢸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⠋⢀⣴⣿⣋⠴⠁⠀⠀⠉⠀⠈⠁⠀⠀⠀⠀⠈⠁⠒⠉⠀⠀⠀⠀⣀⣠⡴⠊⠁⢐⡞⠁⠀⠀⢀⣾⡿⠀⡼⠀⠀⠀⠀
⠀⠀⠀⠀⣰⠁⢠⣿⠟⠀⠀⠀⠀⢠⠖⠐⢦⠀⠀⠀⠀⣀⢀⣀⣠⡤⠴⠒⠢⠈⠉⠀⠈⠀⠀⠀⢨⣣⣀⣤⣶⣿⠟⠁⡰⠃⠀⠀⠀⠀
⠀⠀⠀⠀⡏⠀⣿⡏⠉⢢⠀⠀⠀⠸⢤⣠⠞⠀⣀⡤⢺⡁⠀⠈⡿⠃⠀⣀⣰⡷⣿⣟⣗⣲⣭⠭⠿⠟⠛⠋⠉⢀⡤⠚⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣇⠀⣿⣇⢀⡜⠀⠀⠀⠀⠀⠀⣠⠾⠁⠀⢉⡻⣶⣾⣶⣿⠿⠛⠛⠋⠉⣿⡇⠀⡤⠤⠤⠐⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⡀⠘⢿⣧⣀⠀⠀⠀⠀⠀⡼⠁⣀⡤⣶⣾⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⢻⣇⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢄⠀⠙⠿⢿⣶⣶⣖⣾⡿⠿⠟⠛⠉⠁⢸⢹⠀⠀⠀⠀⠀⠀⠀⠀⢸⣸⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠒⢤⣄⡀⢀⣀⠀⠠⠤⠔⠒⢸⠀⢸⢸⠀⠀⡠⠀⠀⠀⠲⣄⠘⣿⡇⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡴⠒⠉⣉⣈⠉⠑⢦⡀⠀⠀⠀⠀⢸⠀⢸⣾⢀⠎⠀⠀⠀⠀⠀⠈⠳⢿⣷⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⠔⠚⠁⣀⣴⢟⣋⠙⠻⣦⡀⠑⢄⠀⠀⠀⢸⠀⣸⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⡇⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡞⠀⣠⡶⢛⣋⠠⡁⢈⠗⣠⢼⢷⣄⡀⠑⡄⠀⡇⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⢸⣿⡷⢧⣀⠇⠀⠀⠀⠑⠚⠀⠙⢷⡄⢸⢰⠃⢠⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡿⡇⠘⡆⠀⠀⣠⠤⠒⠒⠒⠂⠤⣄⠀⠀
⠈⡄⠘⢷⣄⣀⣀⣀⣰⣏⡹⠀⠀⠀⢀⣼⠇⢸⠛⠀⣼⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⢧⠀⢃⡴⠊⢀⣠⡶⣶⣶⢶⣤⣀⠉⢲
⠀⠙⠦⣀⣈⠉⠉⢹⡏⣿⠛⠶⠶⠶⠟⠁⣠⠎⡇⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠈⠀⣰⢿⣗⡄⠑⠊⠀⠉⣻⡇⠀
⠀⠀⠀⠀⢈⠏⠀⣾⠀⣿⠀⠠⠀⠀⠐⠚⠁⢸⠁⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠘⣿⣄⣈⣐⣭⣦⣴⠾⠋⢀⡼
⠀⠀⠀⠀⡞⠀⣼⠃⢰⡇⠀⡇⠀⠀⠀⠀⠀⢸⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢰⡤⣀⡈⠉⢉⡟⠹⣧⠀⢰⠋⠀
⠀⠀⠀⢰⠁⢰⠏⠀⢸⡇⠀⡇⠀⠀⠀⠀⠀⢸⡀⢸⣸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⢸⠃⠀⢸⠁⢸⡇⠀⠹⣇⠀⡇⠀
⠀⠀⠀⡟⠀⣿⠀⠀⢘⡇⠀⡇⠀⠀⠀⠀⠀⠀⡇⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣻⠀⢸⠀⠀⠸⡆⠘⣧⠀⠀⣿⠀⡇⠀
⠀⠀⠀⢷⠀⢿⣄⣀⣼⠇⢀⡇⠀⠀⠀⠀⠀⠀⠸⡄⠘⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣰⣿⠇⢠⠇⠀⠀⠀⢣⡀⠹⠦⠾⠋⢀⠇⠀
⠀⠀⠀⠈⢦⡀⠉⠉⠁⣀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⡀⠙⠿⣷⣶⣤⣤⣤⣤⣴⣶⣿⠟⠁⣠⠎⠀⠀⠀⠀⠀⠑⠤⠤⠤⠴⠋⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⢄⣀⠈⠉⠉⠉⠉⠉⢁⣀⡤⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")