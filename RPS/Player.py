
# SahuPlayer.py
# Author sahwho
'''
    Represent a Player for Mod/Sim Fall 2024 Project 1 (MBHS)
    A Player has an id (like "P1"), as well as preferences for 2 strategies (which sum to 1.0).
    and keeps track of how many games they've played, plus their total score and average score.
    If you use this class, feel free to rename it Player.py

    Inspiration drawn from the work done by Dr. Andrew Davison (PSU)

    sample usage: p1 = SahuPlayer("P1")
'''

import random

class Player:
    def __init__(self, id):
        self.id = id
        self.prefs = [1/3, 1/3, 1/3] # strategy1 and strategy 2 and stategy 3
        self.currentGameScore = 0
        self.numGamesPlayed = 0
        self.totalScore = 0
        self.averageScore = 0
        self.prevScore = 0
        self.evolvePrefs = [] #strategy 1
        self.prefSizes = []
        self.evolvePrefs2 = [] #strategy 2
        self.prefSizes2 = []
        self.evolvePrefs3 = [] # strategy 3
        self.prefSizes3 = []
        self.points = []
        self.sizes = []

    def getId(self):
        return self.id

    def getPrefs(self):
        return self.prefs

    # no getters needed for currentGameScore, numGamesPlayed, totalScore, or averageScore,
    # since those are used internally within these methods

    # todo: based on the preferences, pseduorandomly select strategy1 or strategy2
    def getStrategy(self):
        r = random.random()
        if r <= self.prefs[0]:
            return 0
        elif (r <= self.prefs[0] + self.prefs[1] and r > self.prefs[0]):
            return 1
        else:
            return 2
    
    # todo: update totalScore, numGamesPlayed, and averageScore
    # this method assumes that a game has been played
    def updateScore(self, strat, score):
        self.updatePrefs(strat, score)
        self.prevScore = score
        self.totalScore += score
        self.numGamesPlayed += 1
        self.averageScore = self.totalScore/self.numGamesPlayed

    # todo: use a formula to update the current Player's preferences
    def updatePrefs(self, strat, score):
        if score > 0:
            self.prefs[strat] += 0.01
            for i in range(3):
                if (i != strat):
                    self.prefs[i] -= 0.005
        elif score < 0:
            self.prefs[strat] -= 0.01
            for i in range(3):
                if (i != strat):
                    self.prefs[i] += 0.005
        else:
            pass

        for i in range(3):
            self.prefs[i] = max(0.0, min(1.0, self.prefs[i]))
        total = sum(self.prefs)
        for i in range(3):
            self.prefs[i] /= total

    # format the object for printing: P1: <p, 1 - p>)
    def __str__(self):
        return f"{self.id}: <{self.prefs[0]}, {self.prefs[1], {self.prefs[2]}}> and they add up to {self.prefs[0] + self.prefs[1] + self.prefs[2]}"