#!/usr/bin/env python
#-*- encoding: utf-8 -*-

"""Command line interpreter right version."""

import sys
import cmd
import random
import os
import pyglet.media
import webbrowser
import time

gachidict = []
with open('gachicmd' + os.sep + 'gachidict.txt') as f:
    gachidict = f.read().splitlines()

soundsdir = os.sep + 'gachicmd' + os.sep + 'sounds'

class GachiShell(cmd.Cmd):
    username = 'slave'
    intro = f'Nice to see you in the gym, {username}.   Type help or ? to list commands.\n'
    prompt = '(gym)> '
    file = None

    def do_fisting(self, arg):
        'fisting is 300$'
        self.username = 'dungeon master'
        path = os.getcwd() + soundsdir
        mp3 = pyglet.media.load(os.path.join(path, "fisting-is-300-.mp3"))
        mp3.play()
        print("Fisting is 300$")

    def do_bosses(self, arg):
        'Who is in gym'
        print("Billy Herrington,", "Van Darkholme,", "Ricardo Milos,", "Mark Wolff,", "Danny Lee")

    def do_do_anal(self, arg):
        'AAAAAAAAAA'
        self.username = 'dungeon master'
        path = os.getcwd() + soundsdir
        mp3 = pyglet.media.load(os.path.join(path, "rip-ears.mp3"))
        mp3.play()
        print("AAAAAAAAAAAA")

    def do_slave(self, arg):
        'for slaves'
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def do_im_master(self, arg):
        'become dungeon master'
        self.username = 'dungeon master'
        path = os.getcwd() + soundsdir
        mp3 = pyglet.media.load(os.path.join(path, "oh-shit-iam-sorry.mp3"))
        mp3.play()
        print(f"Of course you are {self.username}.")

    def do_sounds(self, arg):
        """
        Usage:   sounds [options]

        Default: turn on all sounds

        Options:
        [words]: turn sounds, which has this word(s) in name.
        --list: show list available names of sounds.
        """
        files = os.listdir(os.getcwd() + soundsdir)
        files = [f for f in files if f[-3:] == 'mp3']
        good = 0
        if arg == '--list':
            print(files)
            return
        for f in files:
            tmp = f.replace('-', ' ')
            if arg in tmp:
                path = os.getcwd() + soundsdir
                mp3 = pyglet.media.load(os.path.join(path, f))
                mp3.play()
                time.sleep(mp3.duration)
                good = 1
        if not good:
            print(f'This sound not in gym, {self.username}')

    def do_random_sounds(self, arg):
        'gachi sounds'
        files = os.listdir(os.getcwd() + soundsdir)
        files = [f for f in files if f[-3:] == 'mp3']
        path = os.getcwd() + soundsdir

        mp3 = pyglet.media.load(os.path.join(path, files[random.randint(0, len(files) - 1)]))
        mp3.play()

    def do_phrase(self, arg):
        'random gachi phrase'
        print(gachidict[random.randint(0, len(gachidict) - 1)][3:-3])

    def do_fuckyou(self, arg):
        'Go out from gym'
        print(f'Fisting you soon, {self.username}\n')
        self.close()
        return True
    
    def do_exit(self, arg):
        'Go out from gym'
        return self.do_fuckyou(arg)

    def close(self):
        if self.file:
            self.file.close()
            self.file = None

def main():
    GachiShell().cmdloop()

if __name__ == '__main__':
    sys.exit(main())
