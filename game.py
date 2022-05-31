money = 0
smallbackpack = 30
stick_weapon = 0
rustysword_weapon = 0
shortsword_weapon = 0
claymore_weapon = 0

def goback2():
                print("you walk for a bit until you find a way to the right you can either continue forward go right or go back")
                answer2 = input()
                if answer2 == ("go back"):
                    goback()
                if answer2 == ("continue forward"):
                    print("you continue walking humming a tune as you go doesnt last long though")
                    print("as now you come to a wall and a right turn you can either turn right or go back")
                    answer3 =input()
                    if answer3 == ("go back"):
                        goback2()
                    if answer3 == ("turn right"):
                        print("you walk for a bit until you hear talking and see a hole in the wall")
                        print("it could be enemies or friends but no clue do you want to enter or continue forward?")
                        answer4 = input()
                        if answer4 == ("enter"):
                            print("you idiot.... is what i would say if you didnt just walk into a shop")
                            print("theres an older looking man behind the counter and a traveler of sorts talking to him")
                            print("the traveler walks past you as hes about to leave though he stops 'you arent from round here are you'")
                            print("you say nothing 'look if you want something usefull from here you'll be searching for days.... altough i guess you dont have much of a choice'")
                            print("'here take this' he throws a small backpack at you then leaves")
                            money = 0
                            stick = 2
                            rustysword = 10
                            shortsword = 20
                            claymore = 30
                            smallbackpack = 30
                            money += smallbackpack
                            print("you approach the counter the man glances at you then at some sort of tablet")
                            print("not looking away from his tablet he points at another on the counter near him")
                            print("you have a look")
                            print("""
##############################
# cash = ${}                 #
#                            #
# stick = ${}                #
#                            #
# rusty sword = ${}          #
#                            #
# short sword = ${}          #
#                            #
# claymore = ${}             #
#                            #
# leave                      #
##############################
to buy something go buy then the item you want to purchase if you want to leave go leave
""".format(money, stick, rustysword, shortsword, claymore))
                            shopanswer = input()
                            if answer == ("buy stick"):
                            stick_weapon += 1

                            if answer == ("buy rusty sword"):
                            rustysword_weapon += 1

                            if answer == ("buy short sword"):
                            shortsword_weapon += 1

                            if answer == ("buy claymore"):
                            claymore_weapon += 1

                            if answer == ("leave"):
                            print ("you just kinda walk out not saying anything")
def goback():
        print("you can walk ahead or cry on the ground")
        answer = input()
        if answer == ("walk ahead"):
            goback2()
        if answer == ("cry"):
            print("you drop to the floor and cry for about well you dont know cause you dont have any way of telling the time")
            print("you finally being done crying get up and atem")
            goback()




print("""
###########################################################
###########################################################
##            #                                      #   ##
##            #  #####MAZE#MADNESS #######  #######  #   ##
###############  #                 #     #  #     #  ######
##               ####A#TALE#OF#MAZE#######  #     #       #
##################                          #     #########
###########################################################
###########################################################
""")
print("disclaimer you will be given a map of the maze but no character icon")
print("this means that you have to guess your location in the maze instead of")
print("being directly told you may find shortcuts in the maze but there is also")
print("a chance to run into loops and dead ends so be careful of where you're headed")

print("early testing phases atm")
print("you wake up surrounded by walls on all sides until you turn around and realise you're only surrounded on 3 sides")

            
goback()
goback()
goback2()
