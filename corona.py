import time
import random


def print_pause(sentence):
    print(sentence)
    time.sleep(2)


def validation(prompt):
    while True:
        response = input(prompt)
        if response == "1":
            return response
        elif response == "2":
            return response
        else:
            print_pause("Please select either 1 or 2")


# def score(points):
#     # Used to increment the points scored by player
#     points += 1
#     return points


def right_score(points):
    # Prints and returns incremented score if player response is correct
    newPoints = points
    newPoints += 1
    print("Your score is "+str(newPoints))
    return newPoints


def wrong_score(newPoints):
    # Prints the score of player if response incorrect
    # score not incremented
    print_pause("Your score is "+str(newPoints))


def right_answer():
    # The response when the player makes a right choice
    print_pause("Well done for considering your safety and "
                "the safety of others around you")


def wrong_answer():
    # The response when the player makes a wrong choice
    print_pause("Your irresponsible behavior could potentially put "
                "your life and the life of others at risk")


def expensive():
    # When player refuses to take an important object
    print_pause("You might regret doing that and they cost a "
                "fortune at the shops")


def image():
    # When a player does not wear face mask
    print_pause("Is it worth worrying about your image "
                "during this critical period")


def prepared():
    # When they player has the required equipment
    print_pause("You are well prepared")


def play_again():
    response = validation("If you would you like to play again, choose 1 or"
                          " select 2 to exit\n")
    if response == "1":
        game()
    else:
        print_pause("Bye Bye")
        exit()


def intro(points, objects):
    # Sets the scene for the game and explains the objective of the game
    newPoints = points
    print_pause("Greetings comrade")
    print_pause("This is a day in the life of living during the"
                " corona-virus outbreak")
    print_pause("Lets see if you can remember to do the right things")
    home(newPoints, objects)


def home(newPoints, objects):
    # The interactive part of the game starts here
    options = ["yes", "no"]
    print_pause("You are getting ready to leave the house")
    print_pause("The government has issued warnings")
    print_pause("You say goodbye to your loved ones")
    print_pause("You don't remember whether you packed hand sanitizer"
                " the night before")
    result = random.choice(options)
    if result == "yes":
        prepared()
        right_answer()
        newPoints = right_score(newPoints)
        objects.append("hand_santizer")
    else:
        print_pause("You don't have hand sanitizer and you are running late")
        response = validation("Are you going to quickly get hand sanitizer?\n"
                              "Or leave the house with out getting any?\n"
                              "Type 1 if you choose to get some or type 2 to"
                              " leave it\n")
        if "1" in response:
            right_answer()
            newPoints = right_score(newPoints)
            objects.append("hand_santizer")
        else:
            wrong_answer()
            expensive()
            wrong_score(newPoints)

    print_pause("You don't remember whether you packed your "
                "face mask")
    result = random.choice(options)
    if result == "yes":
        prepared()
        right_answer()
        newPoints = right_score(newPoints)
        objects.append("face_mask")
    else:
        print_pause("You don't have your face mask and you are running late")
        response = validation("Are you going to go and get it?\n"
                              "Or leave the house with out taking it\n"
                              "Type 1 if you choose to get it or 2 to "
                              "leave it\n")
        if "1" in response:
            right_answer()
            newPoints = right_score(newPoints)
            objects.append("face_mask")
        else:
            wrong_answer()
            expensive()
            wrong_score(newPoints)
    catching_bus(newPoints, objects)


def catching_bus(newPoints, objects):
    print_pause("You are now outside trying to catch the bus")
    print_pause("You ponder whether you should put your face mask on\n"
                "You do not want to look stupid")
    print_pause("You check your bag to see whether you brought it")
    if "face_mask" in objects:
        prepared()
        response = validation("Are you going to put your face mask on or "
                              "not?\nType 1 if you choose to put it on or"
                              " 2 to leave it\n")
        if response == "1":
            right_answer()
            newPoints = right_score(newPoints)

        else:
            wrong_answer()
            image()
            wrong_score(newPoints)

    else:
        print_pause("You did not bring it anyway")

    print_pause("You are queuing for the bus")
    print_pause("Someone stands really close to you")

    response = validation("Are you going to maintain the two meter social "
                          "distancing rule or do you think that "
                          "would be rude?\nType 1 if you choose to maintain"
                          " the social distancing rule on or 2 to be polite"
                          " and continue standing close to him\n")
    if response == "1":
        right_answer()
        newPoints = right_score(newPoints)

    else:
        wrong_answer()
        image()
        wrong_score(newPoints)
    work_entrance(newPoints, objects)


def work_entrance(newPoints, objects):
    options = ["yes", "no"]
    print_pause("You are back at work, another day another dollar")
    print_pause("Sometimes, they carry out random checks to see if you "
                "have your face mask and hand sanitizer")
    result = random.choice(options)
    if result == "yes":
        print_pause("You are now being asked to show to the inspector "
                    "that you have what is being asked for")
        if "face_mask" in objects and "hand_santizer" in objects:
            prepared()
            right_answer()
            newPoints = right_score(newPoints)

            work_floor(newPoints, objects)
        elif "face_mask" in objects and "hand_santizer" not in objects:
            print_pause("You need to go to the local shop and"
                        " buy hand sanitizer")
            shop(newPoints, objects)
        elif "face_mask" not in objects and "hand_santizer" in objects:
            print_pause("You need to go to the local shop and buy a "
                        "face mask")
            shop(newPoints, objects)
        else:
            print_pause("You need to go to the local shop and buy a"
                        " face mask and hand sanitizer")
            shop(newPoints, objects)

    else:
        print_pause("You are lucky there are no checks on this occasion")
        work_floor(newPoints, objects)


def shop(newPoints, objects):
    print_pause("You are now at the local shop")
    supplies = ["available", "not_available"]

    outcome = random.choice(supplies)

    if outcome == "available":
        stocks_available(newPoints, objects)



def stocks_available(newPoints, objects):
    print_pause("Luckily they have stocks")
    print_pause("The attendant asks you what you want")

    while True:
        choice = validation("Select 1 if you want hand sanitizer or 2 if you"
                            " want a face mask\n")
        if choice == "1":
            print_pause("The shop keeper asks you to pay a lot for a "
                        "small bottle")

            response = validation("Are you going to buy it at "
                                  "this high price bearing in mind not "
                                  "having one could mean being denied"
                                  " entry into work\n"
                                  "Type 1 if you choose to buy one "
                                  "or 2 to not buy one\n")
            if response == "1" and "hand_santizer" in objects:
                print_pause("You remember you already have a bottle")
            elif response == "1" and "hand_santizer" not in objects:
                right_answer()
                print_pause("You put the hand sanitizer bottle in your bag")
                objects.append("hand_santizer")
                newPoints = right_score(newPoints)

            elif response == "2" and "hand_santizer" in objects:
                print_pause("You you already have a bottle so you don't"
                            " need to buy one")
            elif response == "2" and "hand_santizer" not in objects:
                print_pause("OK fine, but this could prevent you from"
                            " gaining entry at work")

        elif choice == "2":
            print_pause("The shop keeper asks you to pay a lot for a "
                        "face mask")
            response = validation("Are you going to buy it at "
                                  "this high price bearing in mind not "
                                  "having one could mean being denied"
                                  " entry into work?\n"
                                  "Type 1 if you choose to buy one "
                                  "or 2 to not buy one\n")

            if response == "1" and "face_mask" in objects:
                print_pause("You remember you already have"
                            "a face mask")
            elif response == "1" and "face_mask" not in objects:
                right_answer()
                print_pause("You put the face mask in your bag")
                objects.append("face_mask")
                newPoints = right_score(newPoints)

            elif response == "2" and "face_mask" in objects:
                print_pause("You you already have a bottle so you don't"
                            " need to buy one")
            elif response == "2" and "face_mask" not in objects:
                print_pause("OK fine, but this could prevent you from"
                            " gaining entry at work")
        if "face_mask" in objects and "hand_santizer" in objects:
            print_pause("You have a face mask and hand sanitizer")
        elif "face_mask" in objects and "hand_santizer" not in objects:
            print_pause("You don't have hand sanitizer")
        elif "face_mask" not in objects and "hand_santizer" in objects:
            print_pause("You don't have a face mask")
        else:
            print_pause("You have nothing")

        response = validation("Do you wish to continue "
                              "shopping?\n"
                              "Type 1 if you want to shop"
                              " or 2 to go back to work\n")
        if response == "1":
            shop(newPoints, objects)
        else:
            work_entrance(newPoints, objects)



def work_floor(newPoints, objects):
    print_pause("You get into work")
    print_pause("There is a sign stating that you should wash your hands "
                "on entry")
    print_pause("You are in a rush")
    choice = validation("Select 1 if you wash your hands, or 2 if you "
                        "think you haven't got time and you need to get on\n")
    if choice == "1":
        right_answer()
        newPoints = right_score(newPoints)
    else:
        wrong_answer()
        wrong_score(newPoints)
    print_pause("You are advised to put your face mask on")

    if "face_mask" in objects:
        choice = validation("Select 1 if you choose to wear it, or 2 if you "
                            "think you look silly and want to avoid "
                            "potential embarrassment\n")
        if choice == "1":
            right_answer()
            newPoints = right_score(newPoints)
        else:
            wrong_answer()
            image()
            wrong_score(newPoints)
    else:
        print_pause("I bet you wish you were more organized")

    print_pause("You are advised to sanitize your hands, you cant wash them"
                " due to not being able to access a wash basin")
    print_pause("It is a busy time")

    if "hand_santizer" in objects:
        print_pause("Can you be bothered to use it?")
        choice = validation("Select 1 can be bothered to use it or 2"
                            " if you would rather not\n")
        if choice == "1":
            right_answer()
            newPoints = right_score(newPoints)
        else:
            wrong_answer()
            wrong_score(newPoints)
    else:
        print_pause("You did not bring any anyways, so you have"
                    " to borrow some else's")
        print_pause("You have to ask your colleagues to use theirs")
        choice = validation("Select 1 if you ask your colleagues or 2 if you"
                            " would rather not\n")
        if choice == "1":
            right_answer()
            newPoints = right_score(newPoints)
        else:
            wrong_answer()
            wrong_score(newPoints)
    print_pause("You are on lunch break")
    print_pause("Your work colleague comes up and sits next to you "
                "violating the social distancing rules")
    print_pause("You feel uneasy")
    choice = validation("Select 1 if you tell him/her to move away or 2 if you"
                        " don't want to look rude\n")
    if choice == "1":
        print_pause("You colleague moves away feeling slightly embarrassed")
        right_answer()
        newPoints = right_score(newPoints)
    else:

        print_pause("You feel embarrassed and others around look at you "
                    "scornfully with contempt")
        wrong_answer()
        wrong_score(newPoints)

    return_home(newPoints, objects)


def return_home(newPoints, objects):
    # The final interactive part of the game
    print_pause("You return home after a long shift")
    print_pause("All you want to do is to eat and watch TV")

    print_pause("You remember you should wash your hands on your return home")
    choice = validation("Select 1 if you wash you hands or 2 if you"
                        " feel tired and cannot be bothered \n")
    if choice == "1":
        right_answer()
        newPoints = right_score(newPoints)
    else:
        wrong_answer()
        wrong_score(newPoints)

    final(newPoints)


def final(newPoints):
    # Gives an score to the player and shows how adhering they are to
    # government guidelines.
    print_pause("Lets see how adhering you are\n")
    points = newPoints

    if points == 1:
        print_pause("Your final score is " + str(points) + " point\n")
    else:
        print_pause("Your final score is " + str(points) + " points\n")

    if points > 8:
        print_pause("You are doing an exemplary job of protecting"
                    " yourself and those around you\n")
    elif points > 6:
        print_pause("You are doing quite a good job of protecting "
                    "yourself and those around you but you need to"
                    " become more vigilant\n")
    else:
        print_pause("You are doing a poor job of protecting yourself and "
                    "those around you.\nYou need to improve your habits "
                    "during this critical time.\nPlease visit the WHO"
                    "website for more information on how to"
                    "protect yourself\n")
    play_again()


def game():
    points = 0
    objects = []
    intro(points, objects)


game()
