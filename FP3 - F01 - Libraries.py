#-------------
#FP3-F01-Libraries
#Hailey-lynn Aldred
#02 April 2025
#Main Code File
#-------------
import time #allows for me to put time breaks inbetween large pieces of code using time.sleep(). I love this module <3
from modules import greetings #importing my .py file 'greetings'
from modules import view #importing my other .py file 'guess'
#----Functions----#
def time_rest():
    print("I am waiting two seconds.")
    time.sleep(2) #waits two seconds
    print("If I don't wait, everything comes out as a block.")
    print("That's really inconvenient for text based games.")
    print("These are all separate lines, but there's no visual difference.")
    print("Now I'm going to add a break.")
    time.sleep(5) #waits five seconds
    print("See?")
    time.sleep(2)
    print("That's much better.")
    time.sleep(2)
    print("You have time to read and proccess what I'm saying.")
    time.sleep(2)
    
def music_tehe():
    print("I am now importing 'greetings'.")
    time.sleep(2)
    greetings.name('Hailey-lynn') #takes the function in greetings.py and puts my argument through
    print("One of my favourite songs is", greetings.music['Ghost'] + '!') #locating the key attached to the value 'Ghost'
    print(greetings.genre) #prints the variable from greetings
    time.sleep(2)

def oh_yeah_numbers():
    print("I am now importing 'view'")
    time.sleep(2)
    num_yes = view.look(13) #accesses the file and passes 13 into the function. The returned value is then saved
    print(num_yes) #prints the returned value
    time.sleep(2)
    num_no = view.look(8)
    print(num_no)
    time.sleep(2)
    print(view.cool) #prints the variable from view

def main():
    time_rest()
    music_tehe()
    oh_yeah_numbers()
#----Main Code----#
main()
