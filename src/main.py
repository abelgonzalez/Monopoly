from asyncio.windows_events import NULL
from itertools import count
from modules.Player import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer
from modules.RealState import RealState
from modules.Board import Board
from modules.Game import Game
import random
import numpy as np
import itertools

# Player init
player1 = ImpulsivePlayer()
player1.SetName("Jogador1 - Impulsivo")
realStateCost = 200
#player1.BuyRealState(realStateCost)


player2 = DemandingPlayer()
player2.SetName("Jogador2 - Exigente")
rentalAmount = 60
#player2.BuyRealState(rentalAmount)


player3 = CautiousPlayer()
player3.SetName("Jogador3 - Cauteloso")
realStateCost = 60
#player3.BuyRealState(realStateCost)


player4 = RandomPlayer()
player4.SetName("Jogador3 - Aleatório")
realStateCost = 90
#player4.BuyRealState(realStateCost)


# Real state init
realState1 = RealState()
realState1.SetName("Edificio 1")
realState1.SetRentalAmount(100)

realState2 = RealState()
realState2.SetName("Edificio 2")
realState2.SetRentalAmount(100)

realState3 = RealState()
realState3.SetName("Edificio 3")
realState3.SetRentalAmount(100)

board1 = Board()
board1.AddRealStateToBoard(realState1)
board1.AddRealStateToBoard(realState2)
board1.AddRealStateToBoard(realState3)

print(board1.GetBoardRealStateList())

# InitBoard and Real State
board = Board()
for i in range(20):
    buildName = "Edificio " + str(i+1)

    realState = RealState()
    realState.SetName("Edificio " + str(i+1))
    realState.SetCostOfSale(float(np.random.randint(low=100, high=400)))
    realState.SetRentalAmount(float(np.random.randint(low=50, high=200)))
    realState.SetOwner(None)
    realState.SetAvaliableToBuy(True)

    board.AddRealStateToBoard(realState)

print(board.GetBoardRealStateList())


# -------> StartGame
playerList = [player1, player2, player3, player4]


# InitRandomPlayerOrder
random.shuffle(playerList)

# Init Players position on board
currentPositionOnBoard = [0]*4

# print(currentPositionOnBoard)

# Main execution
# while len(playerList)!=1:
#    dd=2

index = 0
for player in playerList:

    # ThrowDice()
    diceFace = np.random.randint(low=1, high=6)
    print(diceFace)

    # Update current Player position
    currentPositionOnBoard[index] += diceFace

    # Getting the board
    boardRealStateList = board.GetBoardRealStateList()

    # Getting the real state, foreach player considering their departure point
    currentPositionRealState = boardRealStateList[currentPositionOnBoard[index]]

    print("Current Owner Real State" + str(currentPositionRealState.GetOwner()))
    # Checking if that real state is avaliable to buy, do it, and mark him has not avaliable
    playerBalance = player.CheckBalance()
    realStateCost = currentPositionRealState.GetCostOfSale()
    if (currentPositionRealState.IsAvaliableToBuy() == True and playerBalance <= realStateCost):

        # if (player.GetName())

        player.BuyRealState(currentPositionRealState)
        currentPositionRealState.SetOwner(player)
        # currentPositionRealState.SetAvaliableToBuy(False)

    else:
        print("Player who pays " + player.GetName())
        rental = currentPositionRealState.GetRentalAmount()
        player.WithdrawMoney(rental)
        print("Rental " + str(rental))

        landLord = currentPositionRealState.GetOwner()
        #landLord.AddBalance(rental)
        print("Receiver " + str(landLord))

    print(currentPositionRealState.GetCostOfSale())

    index += 1

    # At the end of each execution, each player gains $100
    player.AddBalance(float (100))


print(currentPositionOnBoard)


for i in board.GetBoardRealStateList():
    boardRealState = i.GetCostOfSale()
    print(boardRealState)
