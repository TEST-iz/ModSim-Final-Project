"""Final Project: Nash Equilibriums (Game 4: RPS)

Author		Eric Shi
Date 		01/20/2026

This file contains the code pertaining to the simulation of Rock Paper Scissors, and the generation of the ternary simplex. 
It will simulate round robin matches of 10 players, with multiple sessions (50) and then graph the evolution of their strategies
in a ternary plot.

AI Usage: None
Sources: https://github.com/marcharper/python-ternary

"""


import sys
from Player import Player
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import ternary

def Logging(filename):
	"""Reads in the file and builds the payoff matrix, game name, and labels.
	Args:
		filename (str): the name of the file to read from
	Returns:
		numChoices (int): number of choices in the game
		labels (list): list of labels for each choice
		gameName (str): name of the game
		payoff (list): payoff matrix for the game"""
	info = []
	payoff = []

	for line in open(sys.argv[1]):
		li = line.strip() 
		if li != "" and not li.startswith("#"):
			info.append(li)

	numChoices = int(info[0])
	gameName = info[1]
	labels = []

	for i in range(numChoices):
		labels.append(info[i + 2].split()[0])
		payoff.append([(int(info[i + 2].split()[j]), int(info[i + 2].split()[j + 1])) for j in range(1, 6, 2)])
	return numChoices, labels, gameName, payoff

def getRoundRobinMatches(players):
	"""Generates all possible round robin matches between players.
	Args:
		players (list): list of Player objects
	Returns:
		matches (list): list of tuples representing matches between players"""
	matches = []
	for p1, p2 in combinations(players, 2):
		matches.append((p1, p2))
	return matches

def playRound(match):
	"""Plays a single round between two players and updates their scores and preferences.
	Args:
		match (tuple): tuple containing two Player objects
	Returns:
		None"""
	p1 = match[0]
	p2 = match[1]

	#check if specific matchup should be logged when graphing eventually
	if ((p1.id, p2.id) in [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]):
		p1.evolvePrefs.append(p1.prefs[0])
		p1.evolvePrefs2.append(p1.prefs[1])
		p1.evolvePrefs3.append(p1.prefs[2])

		p2.evolvePrefs.append(p2.prefs[0])
		p2.evolvePrefs2.append(p2.prefs[1])
		p2.evolvePrefs3.append(p2.prefs[2])
	
	#get strategies and update scores
	p1Strat = p1.getStrategy()
	p2Strat = p2.getStrategy()
	p1.updateScore(p1Strat, payoff[p1Strat][p2Strat][0])
	p2.updateScore(p2Strat, payoff[p1Strat][p2Strat][1])

def returnResults(players):
	"""Simulates multiple sessions of round robin matches between players.
	Args:
		players (list): list of Player objects
	Returns:
		players (list): list of Player objects with updated scores and preferences"""
	matches = getRoundRobinMatches(players)
	for i in range(50):
		for match in matches:
			playRound(match)
	return players

def cleanUpPrefs(players):
	"""Cleans up the preferences of players for graphing.
	Args:
		players (list): list of Player objects"""
	for p in players:
		p.points = [[p.evolvePrefs[i], p.evolvePrefs2[i], p.evolvePrefs3[i]] for i in range(len(p.evolvePrefs))]
		p.points, p.sizes = np.unique(p.points, axis = 0, return_counts=True)

def plotGraphs(players, gameName, labels):
	"""Plots the ternary graphs of player preferences.
	Args:
		players (list): list of Player objects
		gameName (str): name of the game
		labels (list): list of labels for each choice"""
	cleanUpPrefs(players)

	#matches up 1 v 2, 3 v 4, etc
	for i in range(0, 9, 2):
		scale = 1
		figure, tax = ternary.figure(scale=scale)
		tax.set_title("Scatter Plot", fontsize=20)
		tax.boundary(linewidth=2.0)
		tax.scatter(players[i].points, s = players[i].sizes * 5, color='blue', label=f'P{i+1}', alpha = 0.3)
		tax.scatter(players[i+1].points, s = players[i+1].sizes * 5, color='orange', label=f'P{i+2}', alpha = 0.4)
		tax.bottom_axis_label(labels[0], fontsize=10)
		tax.left_axis_label(labels[1], fontsize=10)
		tax.right_axis_label(labels[2], fontsize=10)
		tax.set_title(gameName)
		tax.legend()
		tax.ticks(axis='lbr', linewidth=1, multiple=1)
		tax.show()

#Main Code
if __name__ == "__main__":
	file = sys.argv[1]
	numChoices, labels, gameName, payoff = Logging(file)
	print("Reading from file:", file)
	print("Game Name:", gameName)
	print("Building Payoff Matrix for", numChoices, "choices:", labels)
	print("Payoff Matrix:", payoff)
	players = [Player(1), Player(2), Player(3), Player(4), Player(5), Player(6), Player(7), Player(8), Player(9), Player(10)]
	players = returnResults(players)
	plotGraphs(players, gameName, labels)
