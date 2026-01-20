"""Final Project: Nash Equilibriums (Game 1, 2, 3: PD, SH, BS)

Author		Eric Shi
Date 		01/20/2026

This file contains the code pertaining to the simulation of Prisoners' Dilema, Stag and Hare, and Battle of Sexes,
and the generation of the ternary simplex. It will simulate round robin matches of 10 players, 
with multiple sessions (50) and then graph the evolution of their strategies in a scatterplot.

AI Usage: None
Sources: None

"""
import sys
from Player import Player
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np

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
		payoff.append([(int(info[i + 2].split()[1]), int(info[i + 2].split()[2])), (int(info[i + 2].split()[3]), int(info[i + 2].split()[4]))])
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
	if ((p1.id, p2.id) in [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]):
		p1.evolvePrefs.append(p1.prefs[0])
		p2.evolvePrefs.append(p2.prefs[0])
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
	for i in range(2000):
		for match in matches:
			playRound(match)
	return players

def cleanUpPrefs(players):
	"""Cleans up the preferences of players for graphing.
	Args:
		players (list): list of Player objects"""
	for p in players:
		p.evolvePrefs2 = [1 - pref for pref in p.evolvePrefs]
		p.evolvePrefs, p.prefSizes = np.unique(p.evolvePrefs, return_counts=True)
		p.evolvePrefs = np.flip(p.evolvePrefs)
		p.prefSizes = np.flip(p.prefSizes)
		p.evolvePrefs2, p.prefSizes2 = np.unique(p.evolvePrefs2, return_counts=True)

def plotGraphs(players, gameName, labels):
	"""Plots the ternary graphs of player preferences.
	Args:
		players (list): list of Player objects
		gameName (str): name of the game
		labels (list): list of labels for each choice"""
	cleanUpPrefs(players)
	for i in range(0, 9, 2):
		P1x = players[i].evolvePrefs
		P1y = players[i].evolvePrefs2
		P1sizes = players[i].prefSizes * 10
		P2x = players[i+1].evolvePrefs
		P2y = players[i+1].evolvePrefs2
		P2sizes = players[i+1].prefSizes * 10

		fig, ax = plt.subplots()
		ax.scatter(P1x, P1y, s=P1sizes, c='blue', label=f'P{i+1}', alpha=0.3)
		ax.scatter(P2x, P2y, s=P2sizes, c='orange', label=f'P{i+2}', alpha=0.4)
		ax.set_xlabel(labels[0], fontsize=10)
		ax.set_ylabel(labels[1], fontsize=10)
		ax.set_title(gameName)

		# show grid
		ax.grid(True)
		p1LegendX = [0.5]
		p1LegendY = [0.5]
		p1LegendSize = [50]
		p1CollectionLegend = ax.scatter(p1LegendX, p1LegendY, s=p1LegendSize, c='blue', alpha=0.3)

		p2LegendX = [0.5]
		p2LegendY = [0.5]
		p2LegendSize = [50]
		p2CollectionLegend = ax.scatter(p2LegendX, p2LegendY, s=p2LegendSize, c='orange', alpha=0.4)

		plt.legend([p1CollectionLegend, p2CollectionLegend], [f'P{i+1}', f'P{i+2}'])
		# end legend code

		# show plot
		plt.show()
				
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