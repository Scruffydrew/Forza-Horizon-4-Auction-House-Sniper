from python_imagesearch.imagesearch import *
from pynput.keyboard import Key, Controller
from datetime import datetime
import time
import sys

# Stop the print command from showing up in the console
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Start of Code
print("Welcome to the Forza Auction House Sniper Bot")
time.sleep(2)
print("Starting program")
time.sleep(2)

# Activates the print block function
blockPrint()

keyboard = Controller()

keyy = "y" # Used to press down and release the 'y' key
kdown = "down" # Used to press down and release the 'down arrow' key
keyenter = "enter" # Used to press down and release the 'enter' key

ahsearch = imagesearch("ahsearch.png") # Search for the image 'ahsearch.png' on your screen
sconfirm = imagesearch("searchconfirm.png") # Search for the image 'searchconfirm.png' on your screen

#print("position, ahsearch: ", ahsearch[0], ahsearch[1])
#print("position, sconfirm: ", sconfirm[0], sconfirm[1])
#print("position, car: ", car[0], car[1])

cat = 0 # Used to make the program loop
turbo = 0 # Used to enter the ah menu
Immortal_Snail = 1 # Used to confirm the settings chosen in the auction house menu
supercharger = 1 # Used to select the car and purchase it from the auction house
chinas_population = 0 # Used to back out of the buy-out screen and return to the start of the script

while cat == 0: # Allows the program to loop
    print("Line: 40")
    #print("cat: " + str(cat))
    #print("turbo: " + str(turbo))
    #print("Immortal Snail: " + str(Immortal_Snail))
    #print("supercharger: " + str(supercharger))
    time.sleep(1.2)
    while turbo == 0 and ahsearch[0] != -1:
        start = time.time()
        print("Line: 48")
        #print("position : ", ahsearch[0], ahsearch[1])
        keyboard.press(Key.enter) # Enters auction house menu
        keyboard.release(Key.enter)
        Immortal_Snail = 0 # Allows the 'while Immortal_Snail == 0:' and following lines of code to run
        turbo = 1 # Stops the 'while turbo == 0 and ahsearch[0] != -1:' and following lines of code from running

    while Immortal_Snail == 0:
        print("Line: 56")
        sconfirm = imagesearch("searchconfirm.png")
        if sconfirm[0] != -1:
            print("Line: 59")
            #print("position : ", sconfirm[0], sconfirm[1])
            keyboard.press(Key.enter) # Confirms if you are in ah and searches for a car
            keyboard.release(Key.enter)
            supercharger = 0 # Allows the 'while supercharger == 0:' and following lines of code to run
            Immortal_Snail = 1 # Stops the 'while Immortal_Snail == 0:' and following lines of code from running
            
    while supercharger == 0:
        print("Line: 67")
        Rear_Window = imagesearch("ah.png") # Checks to see if you are in the auction house - viewing the cars up for auction
        if Rear_Window[0] != -1:
            car = imagesearch('auctiondetails.png') # Search for the image of the rarity of the desired car on your screen
            #print("position, car: ", car[0], car[1])
            if car[0] != -1:
                print("Line: 73")
                #print("car stage achieved!!!")
                keyboard.press(keyy) # Auction house options
                keyboard.release(keyy)
                print("Line: 77")
                time.sleep(.3)
                keyboard.press(Key.down) # Move to Buy-out
                keyboard.release(Key.down)
                print("Line: 81")
                time.sleep(.2)
                keyboard.press(Key.enter) # Opens Buy-out
                keyboard.release(Key.enter)
                print("Line: 85")
                Budget_Shaeden = imagesearch_loop("placebid.png", .1)  # Search for the image 'placebid.png' on your screen
                if Budget_Shaeden[0] != -1:
                    print("Line: 88")
                    keyboard.press(Key.enter) # Buys the car
                    keyboard.release(Key.enter)
                    purchase = time.time()
                    print("Line: 92")
                    supercharger = 1 # Stops the 'while supercharger == 0:' and following lines of code from running
                    chinas_population = 1 # Allows the 'while chinas_population == 1:' and following lines of code to run
            else: # If there is no car avaliable for purchase on the auction house
                print("Line: 96")
                #print("image not found")
                keyboard.press(Key.esc) # Backs out of the auction house, to allow it to have another go at searching
                keyboard.release(Key.esc)
                print("Line: 100")
                # Resets all variables that are stopping previous lines of code from running
                turbo = 0
                Immortal_Snail = 1
                chinas_population = 0
                supercharger = 1
        while chinas_population == 1:
            print("Line: 107")
            time.sleep(6.4)
            print("Line: 109")
            succ = imagesearch_loop("succ.png", .1)  # Search for the image 'succ.png' on your screen
            if succ[0] != 0:
                print("Line: 112")
                # Gets the current time and prints it in the console
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                #print("Current Time: ", current_time)
                # Elapsed time since last purchase
                elapse = str(purchase - start)
                # Gets the time since last purchase and prints it in the console
                #print("Time since last purchase: ", purchase - start)
                # Log current time and elapsed time since last pruchase in text file
                f = open('log.txt', 'a')
                f.write(f"Current Time: " + current_time + " Time Elapsed: " + elapse + " s" + "\n")
                f.close()
                print("Line: 125")
            buyout = imagesearch("buyout.png")  # Search for the image 'buyout.png' on your screen
            if buyout[0] != 0:
                print("Line: 128")
                keyboard.press(Key.enter) # Backs out of the successful buy-out screen
                keyboard.release(Key.enter)
                #print("china has been breached!!")
                print("Line: 132")
                time.sleep(.7)
                print("Line: 134")
                #print("china has been breached!!")
                keyboard.press(Key.esc) # Backs out of the auction house buy menu
                keyboard.release(Key.esc)
                print("Line: 138")
                time.sleep(.7)
                print("Line: 140")
                #print("china has been breached!!")
                keyboard.press(Key.esc) # Returns to start location, before entering the search for the desired car
                keyboard.release(Key.esc)
                print("Line: 144")
                # Resets all variables that are stopping previous lines of code from running
                turbo = 0
                Immortal_Snail = 1
                supercharger = 1
                chinas_population = 0
                cat = 0
                print("Line: 151")
                # Restarts the script
                continue