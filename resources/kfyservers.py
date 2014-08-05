#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
import requests
from bs4 import BeautifulSoup

masterUrl = "http://www.killfunyeah.com/kfy_master.php"
statusUrl = "http://www.killfunyeah.com/kfy_master_status.php"

def getSoup(url):
    """Gets the BeautifulSoup object for whatever is located at [url]."""
    r = requests.get(url)
    return BeautifulSoup(r.text)

def tdsToDict(tds):
    """Converts a <td>s array by getServerRows() to a dictionary."""
    numPlayers = tds[2]
    numPlayers = [int(x) for x in numPlayers.split('/')]
    numPlayers += [0] * (2 - len(numPlayers))
    
    return {
        'name': tds[0],
        'gamemode': tds[1],
        'numplayers': numPlayers[0],
        'maxplayers': numPlayers[1],
        'players': tds[3]
    }

def getServerTrs(url=masterUrl):
    """Gets the server <tr>s at [url]."""
    soup = getSoup(url)
    return soup.find('table').find_all('tr')
def getServerRows(url=masterUrl): # Note: does not return a BeautifulSoup object.
    """Get the server info rows at [url] and return a list of parsed data for every server.
    
    The return format is a list of one:
    ["Server name", "Gamemode", "Number of players", [u'Player', u'List']]
    per server."""
    rows = getServerTrs(url)
    tds = [] # More like tr td lists, but...
    # A tds entry is formatted as ["Server name", "Gamemode", "Number of players", [u'Player', u'List']]
    
    # J forgot to close a <td> and <tr> tag in the HTML, so this is needed...
    lobbyTds = ["Lobby", ""]
    lobbyTds.append(re.split(r"[<>]+", str(rows[0]))[9]) # Getting number of players, yo.
    lobbyTds.append([])
    tds.append(lobbyTds)
    # ---
    
    for i, tr in enumerate(rows[1:], 1):
        if i % 2: # If the row is player images (odd rows)
            playerList = []
            for img in tr.find_all('img'):
                playerList.append(img.attrs['title'])
            tds[-1][3] += playerList 
        else:
            temptds = [x.get_text() for x in tr.find_all('td')]
            tds.append(temptds + [[]])
    return tds
    
def getServerInfoList(serverRows=None):
    """Gets a server info list from [serverRows] (or a new getServerRows() by default), where
    the info is in dictionary form."""
    if not serverRows:
        serverRows = getServerRows()
    
    serverList = []
    for tds in serverRows:
        if tds[2].strip(): # The [2] is actually arbitrary - any obligatory field could be used.
            serverList.append(tdsToDict(tds))
    
    return serverList

def getPlayers(serverInfoList=None):
    """Gets a list of all players currently online."""
    if not serverInfoList:
        serverInfoList = getServerInfoList()
    players = []
    for server in serverInfoList:
        players += server['players']
    return players
    
def getStatusOf(parameter, url=statusUrl):
    """Gets the status of [parameter] from [url]. Works in conjunction with J's PHP status getter."""
    url += "?" + parameter
    try:
        return int(getSoup(url).get_text())
    except ValueError: # Change this to return getSoup(url).get_text() if it turns out there's a non-int-returning parameter.
        return None
def numPlayers(url=statusUrl):
    """Returns the current number of online players."""
    return getStatusOf('numPlayers', url)
def numServers(url=statusUrl):
    """Returns the current number of online servers."""
    return getStatusOf('numServers', url)