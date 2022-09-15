from calendar import c
from difflib import restore
from multiprocessing.resource_sharer import stop
import sys
import threading
import time
import tkinter as tk

stop = False

# Class for keeping count of Things
class Things:
    def __init__(self):
        self.count = 0
        try:
            self.restore()
        except:
            pass

    def add(self, amount = 1):
        self.count += amount

    def sub(self, amount):
        self.count -= amount

    def get(self):
        return self.count

    def restore(self):
        try:
            with open("things.txt", "r") as f:
                self.count = float(f.read())
        except:
            pass

    def save(self):
        with open("things.txt", "w") as f:
            f.write(str(self.count))
    
class Window(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.run()
    
    def run(self):
        self.update()
        self.after(100, self.run)

    def create_widgets(self):
        self.thing_count = tk.Label(self)
        self.thing_count["text"] = "Things: " + str(things.get())
        self.thing_count.pack(side="top")

        self.add_thing = tk.Button(self)
        self.add_thing["text"] = "Make a thing"
        self.add_thing["command"] = self.addThing
        self.add_thing.pack(side="top")

        self.megaThing_count = tk.Label(self)
        self.megaThing_count["text"] = "MegaThings: " + str(megaThing.get())
        self.megaThing_count.pack(side="top")

        self.add_megaThing = tk.Button(self)
        self.add_megaThing["text"] = "Make a megaThing"
        self.add_megaThing["command"] = self.addMegathing
        self.add_megaThing.pack(side="top")

        self.thingMaker_count = tk.Label(self)
        self.thingMaker_count.pack(side="top")

        self.buy_thingMaker = tk.Button(self)
        self.buy_thingMaker["command"] = self.buyThingMaker
        self.buy_thingMaker.pack(side="top")

        self.thingMaker_level = tk.Label(self)
        self.thingMaker_level.pack(side="top")

        self.upgrade_thingMaker = tk.Button(self)
        self.upgrade_thingMaker["command"] = self.upgradeThingMaker
        self.upgrade_thingMaker.pack(side="top")

        self.megaThingMaker_count = tk.Label(self)
        self.megaThingMaker_count.pack(side="top")

        self.buy_megaThingMaker = tk.Button(self)
        self.buy_megaThingMaker["command"] = self.buyThingMaker
        self.buy_megaThingMaker.pack(side="top")
        
        self.megaThingMaker_level = tk.Label(self)
        self.megaThingMaker_level.pack(side="top")

        self.upgrade_megaThingMaker = tk.Button(self)
        self.upgrade_megaThingMaker["command"] = self.upgradeThingMaker
        self.upgrade_megaThingMaker.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.quit)        
        self.quit.pack(side="bottom")

    def addThing(self):
        things.add()

    def addMegathing(self):
        megaThing.add()

    def buyThingMaker(self):
        if things.get() >= thingMakers.cost:
            thingMakers.buy()

    def upgradeThingMaker(self):
        if things.get() >= thingMakers.upgradeCost:
            thingMakers.upgrade()

    def buyMegaThingMaker(self):
        if megaThing.get() >= megaThingMaker.cost:
            megaThingMaker.buy()
    
    def upgradeMegaThingMaker(self):
        if megaThing.get() >= megaThingMaker.upgradeCost:
            megaThingMaker.upgrade()
        
    def update(self):
        self.thing_count["text"] = "Things: " + str(things.get())
        self.megaThing_count["text"] = "MegaThings: " + str(megaThing.get())
        self.thingMaker_count["text"] = "ThingMaker count: " + str(thingMakers.get())
        self.thingMaker_level["text"] = "ThingMaker level: " + str(thingMakers.getLevel()) + " | Cooldown: " + str(thingMakers.delay)
        self.buy_thingMaker["text"] = "Buy a thing maker for " + str(thingMakers.cost) + " things"
        self.upgrade_thingMaker["text"] = "Upgrade thing maker for " + str(thingMakers.upgradeCost) + " things"
        self.megaThingMaker_count["text"] = "MegaThingMaker count: " + str(megaThingMaker.get())
        self.megaThingMaker_level["text"] = "MegaThingMaker level: " + str(megaThingMaker.getLevel()) + " | Cooldown: " + str(megaThingMaker.delay)
        self.buy_megaThingMaker["text"] = "Buy a megaThing maker for " + str(megaThingMaker.cost) + " megaThings"
        self.upgrade_megaThingMaker["text"] = "Upgrade megaThing maker for " + str(megaThingMaker.upgradeCost) + " megaThings"
        #disable buy if not enough things
        if things.get() < thingMakers.cost:
            self.buy_thingMaker["state"] = "disabled"
        else:
            self.buy_thingMaker["state"] = "normal"
        if megaThing.get() < megaThingMaker.cost:
            self.buy_megaThingMaker["state"] = "disabled"
        else:
            self.buy_megaThingMaker["state"] = "normal"
        #disable upgrade if not enough things
        if things.get() < thingMakers.upgradeCost or thingMakers.get() == 0:
            self.upgrade_thingMaker["state"] = "disabled"
        else:
            self.upgrade_thingMaker["state"] = "normal"
            self.buy_megaThingMaker["text"] = "Get thingMaker to max level to unlock"
        if thingMakers.delay < 0.3:
            self.upgrade_thingMaker["state"] = "disabled"
            self.upgrade_thingMaker["text"] = "ThingMaker max level"
            self.buy_megaThingMaker["state"] = "normal"
            self.buy_megaThingMaker["text"] = "Buy a megaThing maker for " + str(megaThingMaker.cost) + " megaThings"
        if megaThing.get() < megaThingMaker.upgradeCost or megaThingMaker.get() == 0:
            self.upgrade_megaThingMaker["state"] = "disabled"
        else:
            self.upgrade_megaThingMaker["state"] = "normal"
        if megaThingMaker.delay < 0.3:
            self.upgrade_megaThingMaker["state"] = "disabled"
            self.upgrade_megaThingMaker["text"] = "MegaThingMaker max level"

    def quit(self):
        things.save()
        print("Saved things")
        thingMakers.save()
        print("Saved thingMakers")
        megaThing.save()
        print("Saved megaThing")
        megaThingMaker.save()
        print("Saved megaThingMaker")
        global stop
        stop = True
        self.master.destroy()

class ThingMaker:
    # Create thread to make things 
    def makeThings(self):
        global stop
        while stop != True:
            #handle exit command
            if self.level > 0:
                time.sleep(self.delay)
                things.add(self.count)
                print("Made " + str(self.count) + " things")

    def __init__(self):
        self.level = 0
        self.count = 0
        self.delay = 3
        self.cost = 5
        self.upgradeCost = 20
        try:
            self.restore()
        except:
            pass
        makeThread = threading.Thread(target=self.makeThings)
        makeThread.start()

    def get(self):
        return self.count

    def buy(self):
        self.count += 1
        things.sub(self.cost)
        self.cost *= 1.2

    def upgrade(self):
        self.level += 1
        self.delay -= 0.1
        things.sub(self.upgradeCost)
        self.upgradeCost *= 1.1

    def getLevel(self):
        return self.level

    def restore(self):
        try:
            with open("thingMakers.txt", "r") as f:
                data = f.read().split(':')
                self.level = int(data[0])
                self.count = int(data[1])
                for _ in range(0, self.level):
                    self.delay -= 0.1
                    self.upgradeCost *= 1.1
                for _ in range(0, self.count):
                    self.cost *= 1.2
        except:
            pass

    def save(self):
        with open("thingMakers.txt", "w") as f:
            f.write(str(self.level) +':'+ str(self.count))

class MegaThings:
    def __init__(self):
        self.count = 0
        try:
            self.restore()
        except:
            pass

    def add(self, amount = 1):
        self.count += amount

    def sub(self, amount):
        self.count -= amount

    def get(self):
        return self.count

    def restore(self):
        try:
            with open("megaThings.txt", "r") as f:
                self.count = float(f.read())
        except:
            pass

    def save(self):
        with open("megaThings.txt", "w") as f:
            f.write(str(self.count))

class MegaThingMaker:
    # Create thread to make things 
    def makeThings(self):
        global stop
        while stop != True:
            #handle exit command
            if self.level > 0:
                time.sleep(self.delay)
                things.add(self.count)
                print("Made " + str(self.count) + " megaThings")

    def __init__(self):
        self.level = 0
        self.count = 0
        self.delay = 5
        self.cost = 20
        self.upgradeCost = 40
        try:
            self.restore()
        except:
            pass
        makeThread = threading.Thread(target=self.makeThings)
        makeThread.start()

    def get(self):
        return self.count

    def buy(self):
        self.count += 1
        megaThing.sub(self.cost)
        self.cost *= 1.5

    def upgrade(self):
        self.level += 1
        self.delay -= 0.1
        megaThing.sub(self.upgradeCost)
        self.upgradeCost *= 1.3

    def getLevel(self):
        return self.level

    def restore(self):
        try:
            with open("megaThingMakers.txt", "r") as f:
                data = f.read().split(':')
                self.level = int(data[0])
                self.count = int(data[1])
                for _ in range(0, self.level):
                    self.delay -= 0.1
                    self.upgradeCost *= 1.3
                for _ in range(0, self.count):
                    self.cost *= 1.5
        except:
            pass

    def save(self):
        with open("megaThingMakers.txt", "w") as f:
            f.write(str(self.level) +':'+ str(self.count))

def main():
    global things
    things = Things()
    global megaThing
    megaThing = MegaThings()
    global thingMakers
    thingMakers = ThingMaker()
    global megaThingMaker
    megaThingMaker = MegaThingMaker()
    root = tk.Tk()
    root.geometry("400x400")
    app = Window(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()

