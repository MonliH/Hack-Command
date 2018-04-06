import sys
import os
import colorama
import string
from threading import Thread
from time import sleep
from random import uniform, choice, randrange

file = [".cobalt",".py", ".c", ".exe", ".cpp", ".cs", ".js", ".go", ".dll", ".virus", ".trojan", ".txt", ".malware", ".fake"]

def do_color(text):
    print("\x1b[0;32;40m" + text + "\x1b[0m")

def do_red(text):
    print("\x1b[0;31;40m" + text + "\x1b[0m")

def startProgress(title):
    global progress_x
    sys.stdout.write("\x1b[0;34;40m" + title + ": [" + "-"*40 + "]" + chr(8)*41 + "\x1b[0m")
    sys.stdout.flush()
    progress_x = 0

def progress(x):
    global progress_x
    x = int(x * 40 // 100)
    sys.stdout.write("\x1b[0;31;40m" + "#" * (x - progress_x) + "\x1b[0m")
    sys.stdout.flush()
    progress_x = x

def endProgress():
    sys.stdout.write("#" * (40 - progress_x) + "\x1b[0;34;40m" + "]\n" + "\x1b[0m")
    sys.stdout.flush()

colorama.init()

def noInterrupt():
    startProgress("Copying Malware To Bank of America Servers")
    for i in range(101):
        progress(i)
        sleep(uniform(0, 0.07))
    endProgress()
    do_color("Done.")

    startProgress("Activating Viruses")
    for i in range(101):
        progress(i)
        sleep(uniform(0, 0.001))
    endProgress()
    do_color("Done.")

    print("Making Credit Card Files..")
    sleep(1)

    for i in range(6000):
        text = ''.join(choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(50)) + choice(file)
        print("\x1b[{};{};{}m".format(randrange(0, 8), randrange(31, 38), randrange(40, 48)) + text + "\x1b[0m")
    do_color("\nDone.")

    while True:
        amount = input("How many passwords do you want to see (Enter n to leave): ")
        if amount == "n":
            break
        for i in range(int(amount)):
            text = ''.join(choice(string.digits) for _ in range(12))
            password = ''.join(choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(randrange(10, 40)))
            print("Credit Card Number: " + text + "; " + "Password: " + password)

    do_red("you left!!!! how dare you")
    sleep(0.5)
    do_red("I will destroy your computer")
    sleep(0.5)
    startProgress("Copying Malware To {}".format(os.getlogin()))
    for i in range(101):
        progress(i)
        sleep(uniform(0, 0.001))
    endProgress()

    while True:
        text = choice(["virus", "trojan", "fake", "no", "dumb"])
        print("\x1b[{};{};{}m".format(randrange(0, 8), randrange(31, 38), randrange(40, 48)) + text + "\x1b[0m")

a = Thread(target=noInterrupt)
a.start()
a.join()
