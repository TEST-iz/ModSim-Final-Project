
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
        """Initializes a Player object with default preferences and scores.
        Args:
            id (int): the unique identifier for the player"""
        self.id = id
        self.prefs = [0.5, 0.5] # strategy1 and strategy 2
        self.currentGameScore = 0
        self.numGamesPlayed = 0
        self.totalScore = 0
        self.averageScore = 0
        self.evolvePrefs = [] #strategy 1
        self.prefSizes = []
        self.evolvePrefs2 = [] #strategy 2
        self.prefSizes2 = []

    def getId(self):
        return self.id

    def getPrefs(self):
        return self.prefs

    # no getters needed for currentGameScore, numGamesPlayed, totalScore, or averageScore,
    # since those are used internally within these methods

    # todo: based on the preferences, pseduorandomly select strategy1 or strategy2
    def getStrategy(self):
        """Selects a strategy based on the player's current preferences."""
        r = random.random()
        if r <= self.prefs[0]:
            return 0
        else:
            return 1
    
    # todo: update totalScore, numGamesPlayed, and averageScore
    # this method assumes that a game has been played
    def updateScore(self, strat, score):
        """Updates the player's score and preferences after a game.
        Args:
            strat (int): the strategy used in the game
            score (int): the score obtained from the game"""
        self.updatePrefs(strat, score)
        self.totalScore += score
        self.numGamesPlayed += 1
        self.averageScore = self.totalScore/self.numGamesPlayed

    # todo: use a formula to update the current Player's preferences
    def updatePrefs(self, strat, score):
        """Updates the player's preferences based on the strategy used and the score obtained.
        Args:
            strat (int): the strategy used in the game
            score (int): the score obtained from the game"""
        self.prefs[strat] = self.prefs[strat] + (score - self.averageScore)/100
        self.prefs[abs(1 - strat)] = 1 - self.prefs[strat]

        if self.prefs[strat] < 0:
            self.prefs[strat] = 0
            self.prefs[abs(1 - strat)] = 1
        elif self.prefs[strat] > 1:
            self.prefs[strat] = 1
            self.prefs[abs(1 - strat)] = 0
        

    # format the object for printing: P1: <p, 1 - p>)
    def __str__(self):
        """Returns a string representation of the player."""
        return f"{self.id}: <{self.prefs[0]}, {self.prefs[1]}>"