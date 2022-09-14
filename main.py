import random
import sys
import time
from pynput import keyboard

# global vars
things = 0

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()

def spin(length):
    for _ in range(length):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')

def RandomLoad():
    for i in range(5):
        #random between 5 and 20
        jitter = random.randint(5, 20)
        for j in range(jitter):
            sys.stdout.write('-')
            sys.stdout.flush()
            time.sleep(0.2)
        loadJitter = random.randint(3, 20)
        spin(loadJitter)

def printSlow(speed, text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(1/speed)

def print(text):
    sys.stdout.write(text)
    sys.stdout.flush()

def clear():
    print(chr(27) + "[2J")
    print(chr(27) + "[1;1f")

def intro():
    clear()
    printSlow(500, "Welcome to the game")
    time.sleep(3)
    clear()
    printSlow(500, "You are a person")
    time.sleep(1)
    clear()
    printSlow(500, "You are in a room")
    time.sleep(1)
    clear()
    printSlow(500, "You are in a room with a door")
    time.sleep(1)
    clear()
    printSlow(500, "You are in a room with a door and a window")
    time.sleep(1)
    clear()
    printSlow(500, "You are in a room with a door and a window and a table")
    time.sleep(1)
    clear()
    printSlow(1000, "---------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    printSlow(100, "------------ ------------------ ------- | Loading Engine Logic |----    -------   - -----        ---    -         -     ---")
    print("\n")
    printSlow(1000, "---------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("\n")
    print("\n")
    RandomLoad()
    time.sleep(3)
    clear()

def on_press(key):
    try:
        if key.char == 't':
            print("You made a thing!")
            global things 
            things += 1
            
        #handle ctrl+c
        elif key.char == '~':
            sys.exit()
    except AttributeError:
        pass

def main():
    # intro()
    # -- tutorial
    printSlow(100, "What do you do?")
    print("\n")
    printSlow(100, "You make things...")
    print("\n")
    printSlow(100, "When you have enough things, you can make more things...")
    print("\n")
    printSlow(100, "You can make things with the things you have")
    printSlow(100, " and the things you make.")
    print("\n")
    printSlow(500, "Lets make some things!")
    time.sleep(1)
    clear()

    # register the listener

    listner = keyboard.Listener(on_press=on_press)
    listner.start()

    while True:
        print("Things: " + str(things))
        print("\n")
        print("Press 't' to make a thing")
        time.sleep(1)
        clear()

    

if __name__ == '__main__':
    main()