# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:53:00 2019

@author: gvandeyk
"""

from random import choice as rc

def AssignAPlayer(Team, Players):
    chosenPlayer = rc(ListOfPlayers)
    Team.append(chosenPlayer.strip('\n'))
    Players.remove(chosenPlayer)
    

myPath = r'C:\Users\gvandeyk\OneDrive - DXC Production\0 - ANALYSIS'
myDirectory = r'000_Python\Jupyter\Data\MakingTeams'
myPlayersFile = 'players.txt'
myTeamsFile = 'teams.txt'

datafilePlayers = open(myPath + '\\' + myDirectory + '\\' + myFile, 'r')
ListOfPlayers = datafilePlayers.readlines()

ListOfTeams = [[], [], [], []]


TeamIndex = 0
while len(ListOfPlayers) > 0:
    Team = ListOfTeams[TeamIndex]
    AssignAPlayer(Team, ListOfPlayers)
    TeamIndex += 1
    try:
        Team = ListOfTeams[TeamIndex]
    except IndexError:
        TeamIndex = 0

print(ListOfPlayers)
print(ListOfTeams)
