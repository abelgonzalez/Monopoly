from asyncio.windows_events import NULL
from itertools import count
from modules.Player import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer
from modules.RealState import RealState
from modules.Board import Board
from modules.Game import Game
from modules.Utils import GetPlayerByName
import random
import numpy as np
import itertools

# Player init
player1 = ImpulsivePlayer()
player1.SetName("Jogador1 - Impulsivo")

player2 = DemandingPlayer()
player2.SetName("Jogador2 - Exigente")

player3 = CautiousPlayer()
player3.SetName("Jogador3 - Cauteloso")

player4 = RandomPlayer()
player4.SetName("Jogador3 - Aleatório")


# Init Board and Real State
board = Board()
for i in range(20):
    buildName = "Edificio " + str(i+1)

    realState = RealState()
    realState.SetName("Edificio " + str(i+1))
    realState.SetCostOfSale(float(np.random.randint(low=100, high=400)))
    realState.SetRentalAmount(float(np.random.randint(low=50, high=200)))
    realState.SetOwner("")
    realState.SetAvaliableToBuy(True)

    board.AddRealStateToBoard(realState)

# print(board.GetBoardRealStateList())


# -------> StartGame
playerList = [player1, player2, player3, player4]


# InitRandomPlayerOrder
random.shuffle(playerList)

# Init Players position on board
currentPositionOnBoard = [0]*4

# Initially, all players starts at 0
indexBoardPlayer = 0

# Init game loop
quantOfIterationsbyPlayer = 1

# Init board loop
quantOfBoardIterations = 1

# Timeout
timeoutValue = 1000

# Main execution
while (True):
    print("Board iteration #"+str(quantOfBoardIterations))
    print("Iteration #"+str(quantOfIterationsbyPlayer))

    for player in playerList:

        # ThrowDice()
        diceFace = np.random.randint(low=1, high=6)
        print("Current player --> " + player.GetName())
        print("Movements (Dice) --> " + str(diceFace))

        # Update current Player position
        currentPositionOnBoard[indexBoardPlayer] += diceFace

        # In case we arrive to boundaries of game. Ex position 20 of board, then starts
        # at the beggining. Recomendation, use linked list.
        if currentPositionOnBoard[indexBoardPlayer] >= 20:
            currentPositionOnBoard[indexBoardPlayer] -= 20
            # Update board loop
            quantOfBoardIterations += 1

        print("Current board position " +
              str(currentPositionOnBoard[indexBoardPlayer]))

        # Getting the board
        boardRealStateList = board.GetBoardRealStateList()

        # Getting the real state, foreach player considering their departure point
        currentPositionRealState = boardRealStateList[currentPositionOnBoard[indexBoardPlayer]]

        # Checking if that real state is avaliable to buy, do it, and mark him has not avaliable
        playerBalance = player.CheckBalance()
        print("balance = "+str(playerBalance))
        realStateCost = currentPositionRealState.GetCostOfSale()
        print("realStateCost = "+str(realStateCost))
        realStateRent = currentPositionRealState.GetRentalAmount()
        print("realStateRent = "+str(realStateRent))
        ownerName = str(currentPositionRealState.GetOwner())
        print("Owner of this real state " + ownerName)

        # Has the funds and the real state does not have owner
        if (realStateCost <= playerBalance and currentPositionRealState.GetOwner() == ""):

            player.BuyRealState(currentPositionRealState)
            currentPositionRealState.SetOwner(player)
            print(player.GetName() + " is now the owner of " + ownerName)
            print("Owner after buy "+str(currentPositionRealState.GetOwner()))

        # In case of the real state has owner, then pay rent to landlord
        elif (currentPositionRealState.GetOwner() != ""):
            print("Pay rent!")
            print("Player who pays " + player.GetName())
            player.WithdrawMoney(realStateRent)
            print("Rental " + str(realStateRent))

            # Getting landlord/owner player
            ownerPlayer = currentPositionRealState.GetOwner()
            # ownerPlayer.AddBalance(realStateRent)

            # Now, update the owner player to player's list
            playerOwner = GetPlayerByName(ownerPlayer, playerList)
            playerOwner.AddBalance(realStateRent)
            indexOwner = playerList.index(playerOwner)
            playerList[indexOwner] = playerOwner

            print("Receiver " + str(playerOwner))

       
        # In case no funds or negative, declare it in Bankrupt
        if player.CheckBalance() <= 0:
            player.DeclareBankrupt()
            playerList.remove(player)

            # Also, removes all real states from him
            for realState in board:
                if realState.GetOwner() == player:
                    realState.SetOwner("")
            
            
            print("****Player " + str(player.GetName()) + " had declared is in bankrupt***")

            #pass

        # Setting the real state, foreach player considering their departure point
        boardRealStateList[currentPositionOnBoard[indexBoardPlayer]
                           ] = currentPositionRealState

        # At the end of each execution, each player gains $100
        player.AddBalance(float(100))

        print("\n")

    quantOfIterationsbyPlayer += 1

    if (len(playerList) == 1) or (timeoutValue <= quantOfBoardIterations):
        break


print("End of execution!")


# for i in board.GetBoardRealStateList():
#    boardRealState = i.GetCostOfSale()
#    print(boardRealState)
