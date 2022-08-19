import random
from os import system, name

rand = random.randint(0,100)

def clear():

	# for windows
	if name == 'nt':
		_ = system('cls')

	# for mac and linux(here, os.name is 'posix')
	else:
		_ = system('clear')

while True :

    askmy = input("Type a rule to know the rules of the game and tips : ")

    if (askmy == "rule") :
        print("\n" + "I generate a random number and you can ask me questions" + "\n" "and i ask you the questions and you must find number" + "\n")
        print("To know that the number is   even or odd Type e&o " + "\n")
        print("to know the number is bigerthan or smaller than x Type isup" + "\n")
        print("Type cls to clear all text in app" + "\n")
        print("Type is to know your guss is number")
        print("Type divisible to know if x is divisible by another number\n")
#############################################################################
    if (askmy == "e&o"):
        x = rand % 2 

        if (x == 0) :
            num = ("Number is even")
        elif (x != 0):
            num = ("Number is odd")

        print(num)
##########################################################################
    if (askmy == "isup"):
        up = input("Type your number to check for is bigger or is smaller than : ")

        if (up > rand) :
            print("your number is bigger than x")

        elif (up == rand) :
            print("This is it")

        elif (up < rand) :
            print("your number is smmaler than x")
##########################################################################

    if (askmy == "is"):
        Trues = input("Type ypur guss : ")

        if (Trues == rand):
            text = "is it"
        else:
            text = "no"

        print(text)


###########################################################################
    if (askmy == "divisible"):
        know = input("Type number to check is divisible to x : ")

        if (rand % know == 0) :
            div = "is divisible"
        else :
            div = "is not divisible"
            
        print(div)
###########################################################################
    if (askmy == "cls"):
        clear()
########################################################################

