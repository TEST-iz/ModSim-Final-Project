# ModSim-Final-Project

## Project Description
This project attempts to faciliate the emergence of Nash Equlibriums through repeated simulation between 10 players in a round robin style match up. There are four games, Prisoners' Dilema, Stag and Hare, Battle of the Sexes, and Rock Paper Scissors. For the first three, there are 2000 sessions of round robins. For Rock Paper Scissors, there are only 50 sessions of round robins. Each game has a txt file associated with it including relevant information and its payoff matrices. Afterwards, the evolution of the probability of prefences for each players are plotted using either matplotlib or python-ternary, depending on the game. The graphs will show ONlY the evolution of preferences from matchups between the first two players, the next two players, etc, etc. Each player does not know the payoffs until after the game is finished, and will update their preferences accordingly.

### Author
Eric Shi

## Usage
To run the project, you must first determine which game you wish to simulate. Prisoner's Dilema, Stag and Hare, and Battle of the Sexes are located in the Games_1-3 directory. Rock Paper Scissors is located in the Game_4 directory. After you have navigated to the correct direcory, you can run the simulation and generate the graphs using,

`python main.py game.txt`

* `game.txt` = text file associated with specific game (e.g. `pd.txt`, `sh.txt`, `bs.txt`)

You can navigate to the desired directory using one of the commands below

`cd .\Games_1-3\`

or

`cd .\Game_4\`


## Installation 

1. Clone the repository
2. Navigate into the `ModSim-Final-Project` Repository


## Sample Outputs

### Prisoners' Dilemma

![frr](/ModSim-Final-Project/samples/PD_sample.png)

### Stag and Hare 

![frr](/ModSim-Final-Project/samples/SH_sample1.png)
![frr](/ModSim-Final-Project/samples/SH_sample2.png)

### Battle of the Sexes

![frr](/ModSim-Final-Project/samples/BS_sample1.png)
![frr](/ModSim-Final-Project/samples/BS_sample2.png)

### Rock Paper Scissors

![frr](/ModSim-Final-Project/samples/RPS_sample.png)