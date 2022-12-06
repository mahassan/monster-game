#
# #This is the option for when you pick the mushroom path
# 
def mushroom_option():
    print("""I see you want to find the magical mushrooms, follow me.
You follow the monster to a dark part of the forest and see a large patch of mushrooms surrounded by a sharp, spiky fence with a gate and a sign.
The sign has a message on it
		================================================================|
    |To gain access to these fungi you must complete a maths puzzle |
    |                                           /``\                |
    |   To begin the puzzle press this button  |    |               |
    |                                           \,,/                |                                           |
    |===============================================================|
    """)

    mush_gate= input("Type a if you want to press the button or\nType b to hop over the fence and ignore the sign\n>").lower()
    if mush_gate=="a":
        maths_puzz1()
    if mush_gate=="b":
        print("As if it would be that easy!!\nYou grab the fence to hop over it and get an huge electric shock.\nHope you have clean underwear at home.\nThe monster laughs and presses the button for you")
        maths_puzz1()
def maths_puzz1():
    maths_answer1=input("The sign spins around and a maths puzzle is revealed\nType an even prime number.\n>")
    if maths_answer1=="2":
        print("That is the correct answer\nNext question")
        maths_puzz2()
    else:
         print("Wrong answer and that one was easy, try again")
    maths_puzz1()


def maths_puzz2():
    maths_answer2=input("If I add 6 to 11, I get 5. What am I looking at?\n>").lower()
    if maths_answer2!="aclock" and maths_answer2!="clock" and maths_answer2!="a clock":
        print("Wrong answer, try again")
        maths_puzz2()
    else:
        print("Correct, and now the final puzzle\nGet this correct and you may access the mushroom patch")
        maths_puzz3()

def maths_puzz3():
    maths_answer3=input("A grandfather,2 fathers and 2 sons go to the cinema and everyone bought one ticket each.\nHow many tickets were bought?\n>")
    if maths_answer3=="3":
        print("That is the correct answer\nNext question")
        ending_finish()
    else:
         print("Wrong answer, try again")
    maths_puzz3()
# 
# #This is the good ending where you all survive
# 
def ending_finish():
    happy_ending=input("""Your mushroom collecting skills are exemplary.
You successfully create the cure and give it to the monster's sick dog.
The dog leaps up and licks you on the face in excitement.
The monster, equally as excited also leaps up and licks you on the face sending you to the floor with a bump
and a wet face.
'Thank you for curing my dog' says the monster.
'Can I buy you a drink at my favourite pub The Frolicking Maggot?
\nType 'a' to join the monster in the pub or\nType 'b' to head home, you've had enough excitement for the day\n>""").lower()
    tries=1
    while happy_ending!="a" and happy_ending!="b":
        print("That is not a valid option")
        tries+=1
        print(f"This was attempt number {tries} to type a or b. Try again")
        happy_ending=input("Type a to join the monster in the pub or\nType b to head home, you've had enough excitement for the day\n>").lower()

    if happy_ending=="a":
        print(""""
      .======================================.
      | ___ ___ ___               _   _   _  |
      | \_/ \_/ \_/ C|||C|||C||| |-| |-| |-| |
      | _|_ _|_ _|_  ||| ||| ||| |_| |_| |_| |
      '===================================== '
                 =====================                
                |The Frolicking Maggot |      
           .:.   =====================                           
          C|||'                             
        ___|||______________________________
       [____________________________________]
        |   ____    ____    ____    ____   | 
        |  (____)  (____)  (____)  (____)  | 
        |  |    |  |    |  |    |  |    |  | 
        |  |    |  |    |  |    |  |    |  |  
        |  |    |  |    |  |    |  |    |  | 
        |  |____|  |____|  |____|  |____|  | 
        |  I====I  I====I  I====I  I====I  | 
        
        You head off to the pub with the monster and his dog, and become firm friends""")
    if happy_ending=="b":
        print("""
        `'::.
    _________H ,%%&%,
   /\     _   \%&&%%&%
  /  \___/^\___\%&%%&&
  |  | []   [] |%\Y&%'
  |  |   .-.   | ||  
~~@._|@@_|||_@@|~||~~~~~~~~~~~~~
     `''') )'''`
You head off home after a long, interesting day.
You swap numbers with the monster so you can meet up again with your new friend.
""")

    
    play_again=input("""Would you like to play again?\nType y to start again\nOr n to end the game\n>""").lower()
    while play_again!="y" and play_again!="n":
        print("That is not a valid option")
        play_again=input("Would you like to play again?\n>").lower()
    if play_again=="y":
        start_again()
    if play_again=="n":
        print("Thank you for playing {first_name}\nGOODBYE")
        exit()
        
mushroom_option()

mushroom_option()