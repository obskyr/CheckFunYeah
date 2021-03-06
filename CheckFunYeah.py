#!/usr/bin/env python
# -*- coding: UTF-8 -*-

version = '1.0'

import os   # For checking for modules in resources directory
import sys  # -||-
sys.path.insert(0, os.path.join(os.getcwd(), 'resources'))

import imp # To check modules without importing them.
import pip # To install them if they're not there.

def install(package):
    pip.main(['install', '--quiet', package])

# Hard coded dependencies! Yeah!
requiredModules = [['requests', 'requests'], ['bs4', 'beautifulsoup4']]
for module in requiredModules: # For installing needed modules.
    try:
        imp.find_module(module[0])
    except ImportError:
        print "Installing " + module[1] + "..."
        install(module[1])

import kfyservers
import confutil
import time
try:
    import winsound
    soundEnabled = True
except ImportError:
    soundEnabled = False

# --- Import initialization end ---

print "--- CheckFunYeah {0} started! Let's do this! ---".format(version)

def joinLists(lists):
    """Joins [lists] into one and returns the result."""
    uberlist = []
    for l in lists:
        uberlist.extend(l)
    return uberlist
def unique(lists):
    """Returns a list of all the elements that only appear in one of the lists in [lists]."""
    uniques = []
    for i, l in enumerate(lists):
        otherLists = lists[0:i] + lists[i+1:]
        otherLists = joinLists(otherLists)
        for v in l:
            if not v in otherLists:
                uniques.append(v)
    return uniques

noteSound = os.path.join('resources', 'checkit.wav')
config = confutil.getConfig('settings.cfg')
config['Play sound'] = confutil.strToBool(config['Play sound'])
config['Time between server checks (in seconds)'] = int(config['Time between server checks (in seconds)'])
config['Notify on every check'] = confutil.strToBool(config['Notify on every check'])
config['Max number of players to show names of'] = int(config['Max number of players to show names of'])
ignoreList = [x.lower() for x in confutil.getList('ignored.txt')]

prevNumPlayers = -1
prevPlayersOnline = []
while True:
    playersOnline = kfyservers.getPlayers()
    numPlayers = len(playersOnline)
    ignoredOnline = [x for x in playersOnline if x.lower() in ignoreList]
    
    if numPlayers - len(ignoredOnline) > 0:
        if (config['Notify on every check'] or prevNumPlayers <= 0) and config['Play sound'] and soundEnabled:
            # Doesn't really matter when sound is played, since it's asynchronous.
            winsound.PlaySound(noteSound, winsound.SND_FILENAME | winsound.SND_ASYNC)
        if unique([playersOnline, prevPlayersOnline]): # Only notify if the players have changed
            if numPlayers <= config['Max number of players to show names of']: # Print a player list
                print time.strftime("[%H:%M:%S] ", time.localtime()) + ', '.join(playersOnline)
            else:
                print str(numPlayers) + ' players online!'
    elif numPlayers == 0 and prevNumPlayers != 0:
        print time.strftime("[%H:%M:%S] ", time.localtime()) + "No players online at all!"
    elif [x for x in playersOnline if x not in prevPlayersOnline]:
        print time.strftime("[%H:%M:%S] ", time.localtime()) + "No non-ignored players online."
    prevNumPlayers = numPlayers
    prevPlayersOnline = playersOnline
    time.sleep(config['Time between server checks (in seconds)'])
