#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""Command line interpreter right version."""

import sys
import cmd
import random
import os
import pyglet.media
import webbrowser
import time
import datetime as dt
import getpass

gachidict = []
with open("gachicmd" + os.sep + "gachidict.txt") as f:
    gachidict = f.read().splitlines()

heroes = []
with open("gachicmd" + os.sep + "gachiheroes.txt") as f:
    heroes = f.read().splitlines()

soundsdir = os.sep + "gachicmd" + os.sep + "sounds" + os.sep

def myplaysound(sound):
    path = os.path.join(os.getcwd() + soundsdir, sound)
    print(sound[:-4])
    mp3 = pyglet.media.load(path)
    mp3.play()

class GachiShell(cmd.Cmd):
    username = "slave"
    intro = (
        f"Nice to see you in the gym, {username}.   Type help or ? to list commands."
    )
    current_time = dt.datetime.now().time()
    prompt = "\n[" + str(current_time)[:8] + "]--[boss of this gym: " + getpass.getuser() + "]--[gym: " + os.getcwd() + "]\n300$ "
    file = None

    def do_fisting(self, arg):
        "fisting is 300$"
        self.username = "dungeon master"
        myplaysound("fisting-is-300-bucks.mp3")

    def do_choose_hero(self, arg):
        """become gachi hero

        options: -l, --list: show list of hero names"""
        if arg == "--list" or arg == "-l":
            print(heroes)
            return
        if arg.isspace() or arg == "":
            print("You don't print gachihero name, slave")
            return
        for hero in heroes:
            if arg in hero:
                self.username = hero
                print(f"Nice to fuck you, {self.username}")
                return
        print("Gachihero don`t found, slave")

    def do_mansingym(self, arg):
        "Who is in gym"
        l = list(range(0, random.randint(0, len(heroes) - 1)))
        random.shuffle(l)
        for i in l:
            print(heroes[i])

    def do_do_anal(self, arg):
        "AAAAAAAAAA"
        self.username = "dungeon master"
        
        print("AAAAAAAAAAAA")

    def do_slave(self, arg):
        "for slaves"
        print("Gotcha! You`ve been gachirickrolled :)")
        webbrowser.open("https://youtu.be/_rW9a9Z4YbI")

    def do_im_master(self, arg):
        "become dungeon master"
        self.username = "dungeon master"
        myplaysound("oh-shit-iam-sorry.mp3")
        print(f"Of course you are {self.username}.")

    def do_sounds(self, arg):
        """
        Usage:   sounds [options]

        Default: turn on all sounds

        Options:
        [words]: turn sounds, which has this word(s) in name.
        -l, --list: show list available names of sounds.
        """
        files = os.listdir(os.getcwd() + soundsdir)
        files = [f for f in files if f[-3:] == "mp3"]
        good = 0
        if arg == "--list" or arg == "-l":
            print(files)
            return
        for f in files:
            tmp = f.replace("-", " ")
            if arg in tmp:
                path = os.getcwd() + soundsdir
                mp3 = pyglet.media.load(os.path.join(path, f))
                mp3.play()
                time.sleep(mp3.duration)
                good = 1
        if not good:
            print(f"This sound not in gym, {self.username}")

    def do_random_sounds(self, arg):
        "gachi sounds"
        files = os.listdir(os.getcwd() + soundsdir)
        files = [f for f in files if f[-3:] == "mp3" or f[-3:] == "wav"]
        myplaysound(files[random.randint(0, len(files) - 1)])

    def do_phrase(self, arg):
        "random gachi phrase"
        if sys.platform.startswith("linux"):
            print(gachidict[random.randint(0, len(gachidict) - 1)])
        elif sys.platform.startswith("win"):
            print(gachidict[random.randint(0, len(gachidict) - 1)][3:-3])

    def do_fuckyou(self, arg):
        "Go out from gym"
        print(f"Fisting you soon, {self.username}\n")
        self.close()
        return True

    def default(self, arg):
        "Execute basic cmd commmand"
        if arg[:2] == 'cd':
            dir = arg.split()[1]
            path = os.getcwd() + os.sep + dir
            if os.path.exists(path):
                os.chdir(path)
            else:
                print(f"Path {path} doesn't exist")
        else:
            os.system(arg)
    
    def do_makemecum(self, arg):
        "Execute make"
        os.system("make")

    def do_exit(self, arg):
        "Go out from gym"
        return self.do_fuckyou(arg)

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

    def postcmd(self, stop, line):
        """Hook method executed just after a command dispatch is finished."""
        current_time = dt.datetime.now().time()
        self.prompt = "\n[" + str(current_time)[:8] + "]--[boss of this gym: " + getpass.getuser() + "]--[gym: " + os.getcwd() + "]\n300$ "
        return stop


def main():
    GachiShell().cmdloop()


if __name__ == "__main__":
    sys.exit(main())
