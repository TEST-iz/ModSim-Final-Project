# ModSim-Final-Project

## Project Description
This project attempts to faciliate the emergence of Nash Equlibriums through repeated simulation between 10 players in a round robin style match up. There are four games, Prisoners' Dilema, Stag and Hare, Battle of the Sexes, and Rock Paper Scissors. Each game has a txt file associated with it including relevant information and it's payoff matrices. Afterwards, the evolution of the probability of prefences for each players are plotted using either matplotlib or ternary, depending on the game. Each player does not know the payoffs until after the game is finished, and will update their preferences accordingly.

### Author
Eric Shi

## Usage
To run the project, you must first determine which game you wish to simulate. Prisoner's Dilema, Stag and Hare, and Battle of the Sexes are located in the Games_1-3 directory. Rock Paper Scissors is located in the Game_4 directory. After you have navigated to the correct direcory, you can run the simulation and generate the graphs using,

`python main.py game.txt`

* `game.txt` = text file associated with specific game (e.g. `pd.txt`, `sh.txt`, `bs.txt`)

You can navigate the desired directory using the right command below

`cd .\Games_1-3\`

or

`cd .\Game_4\`


## Installation 

1. Clone the repository
2. Navigate into the `ModSim-Final-Project` Repository