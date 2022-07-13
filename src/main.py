
import numpy as np
import statistics

from modules.Game import Game
from modules.Board import Board
from modules.RealState import RealState
from modules.Player import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer


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
    timeoutValue = 1000

    # Simulations
    quantOfSimulations = 300

    # Report vars:
    gamesEndedByTimeOutDict = {}
    timePerGameDict = {}
    playerProbabilitiesDict = {"Jogador1 - Impulsivo": 0, "Jogador2 - Exigente": 0,
                               "Jogador3 - Cauteloso": 0, "Jogador4 - Aleatório": 0}
    playerWinningDict = {}

    # Main execution
    for simIndex in range(quantOfSimulations):

        simStr = str(simIndex+1)

        print("######## Simulation " + simStr +
              " of " + str(quantOfSimulations) + " ########")
        game = Game()
        game.SetGameName("Simulation"+simStr)
        gameEndedByTimeOut, timeGame, playerProbability, winningPlayer = game.StartGame(
            playerList, board, timeoutValue)

        gamesEndedByTimeOutDict["Simulation " + simStr] = gameEndedByTimeOut
        timePerGameDict["Simulation " + simStr] = timeGame

        for key, value in playerProbability.items():
            playerProbabilitiesDict[key] += value

        playerWinningDict["Simulation "+simStr] = winningPlayer

    print("\n")
    print("Final report")
    print("1. Time-out ended games: " +
          str(sum(gamesEndedByTimeOutDict.values())))
    print("2. Median time per game: " +
          str(statistics.median(timePerGameDict.values())))
    print("3. Percent of victories by player: " + str(playerProbabilitiesDict))
    print("4. Winner behaviour: " +
          str(list(playerWinningDict.values())[0]))
