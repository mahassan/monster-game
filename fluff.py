def monster_speech() :
    print("this is what monster says.")
def leg_it() :
    print("you scarper.")
    
choiceone = input("type 'a' to befriend the monster, type 'b' to leg it   ").lower()
while choiceone != "a" or choiceone != "b" :
    choiceone = input("      either 'a' or 'b' please        ").lower()
    if choiceone == "a" :
        monster_speech()
    elif choiceone == "b" :
        leg_it()
