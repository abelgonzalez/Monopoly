from itertools import count
from modules.Player import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer
from modules.RealState import RealState
from modules.Board import Board
from modules.Game import Game
from modules.Utils import GetPlayerByName
import random
import numpy as np
import itertools
import time
import statistics
import collections

if __name__ == "__main__":

    # Player init
    player1 = ImpulsivePlayer()
    player1.SetName("Jogador1 - Impulsivo")
    player2 = DemandingPlayer()
    player2.SetName("Jogador2 - Exigente")
    player3 = CautiousPlayer()
    player3.SetName("Jogador3 - Cauteloso")
    player4 = RandomPlayer()
    player4.SetName("Jogador4 - Aleatório")
    playerList = [player1, player2, player3, player4]

    # Init Board and Real State
    board = Board()
    for i in range(20):
        realState = RealState()
        realState.SetName("Edificio " + str(i+1))
        realState.SetCostOfSale(float(np.random.randint(low=100, high=400)))
        realState.SetRentalAmount(float(np.random.randint(low=50, high=200)))
        realState.SetOwner("")
        realState.SetAvaliableToBuy(True)
        board.AddRealStateToBoard(realState)

    # Timeout
    timeoutValue = 10

    # Simulations
    quantOfSimulations = 50

    # Report vars:
    gamesEndedByTimeOut = 0
    timePerGame = []
    totalTime = 0
    finalPlayerListBeahavior = {}
    finalPlayerProbabilities = {}
    for player in playerList:
        finalPlayerProbabilities[player.GetName()] = 0

    # Main execution
    for simIndex in range(quantOfSimulations):

        print("######## Simulation " + str(simIndex) +
              " of " + str(quantOfSimulations) + " ########")
        game = Game()
        game.SetName("Simulation"+str(simIndex))
        gamesEndedByTimeOut, timePerGame, finalPlayerProbabilitiesStr, winningPlayer = game.StartGame(
            playerList, board, timeoutValue)

    # print("\n")
    #print("Final report")
    #print("1. Time-out ended games: " + str(gamesEndedByTimeOut))
    #print("2. Median time per game: " + str(statistics.median(timePerGame)))
    #print("3. Percent of victories by player: " + str(finalPlayerProbabilities))
    # print("4. Winner behaviour: " +
    #      str(list(finalPlayerListBeahavior.keys())[0]))
