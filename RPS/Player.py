"""Player Class (Game 4: RPS)

Author		Eric Shi
Date 		01/20/2026

This file contains the code pertaining to the player class for RPS. Originally created by Vikash Sahu, and modified by Eric Shi.

AI Usage: None
Sources: Vikash Sahu

"""


import random

class Player:
    def __init__(self, id):
        """Initializes a Player object with default preferences and scores.
        Args:
            id (int): the unique identifier for the player"""
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
        """Selects a strategy based on the player's current preferences."""
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
        """Updates the player's score and preferences after a game.
        Args:
            strat (int): the strategy used in the game
            score (int): the score obtained from the game"""
        self.updatePrefs(strat, score)
        self.prevScore = score
        self.totalScore += score
        self.numGamesPlayed += 1
        self.averageScore = self.totalScore/self.numGamesPlayed

    # todo: use a formula to update the current Player's preferences
    def updatePrefs(self, strat, score):
        """Updates the player's preferences based on the strategy used and the score obtained.
        Args:
            strat (int): the strategy used in the game
            score (int): the score obtained from the game"""
        if score > 0:
            self.prefs[strat] += 0.01
            #update strategies that are not what was chosen
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
        
        #checking bounds and normalizing
        for i in range(3):
            self.prefs[i] = max(0.0, min(1.0, self.prefs[i]))
        total = sum(self.prefs)
        for i in range(3):
            self.prefs[i] /= total

    # format the object for printing: P1: <p, 1 - p>)
    def __str__(self):
        """Returns a string representation of the player."""
        return f"{self.id}: <{self.prefs[0]}, {self.prefs[1], {self.prefs[2]}}> and they add up to {self.prefs[0] + self.prefs[1] + self.prefs[2]}"