from asyncio.windows_events import NULL
from itertools import count
from modules.Player import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer
from modules.RealState import RealState
from modules.Board import Board
from modules.Game import Game
import random
import numpy as np

# Player init
player1 = ImpulsivePlayer()
player1.SetName("Jogador1 - Impulsivo")
realStateCost = 200
player1.BuyRealState(realStateCost)


player2 = DemandingPlayer()
player2.SetName("Jogador2 - Exigente")
rentalAmount = 60
player2.BuyRealState(rentalAmount)


player3 = CautiousPlayer()
player3.SetName("Jogador3 - Cauteloso")
realStateCost = 60
player3.BuyRealState(realStateCost)


player4 = RandomPlayer()
player4.SetName("Jogador3 - Aleatório")
realStateCost = 90
player4.BuyRealState(realStateCost)


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
    realState.SetOwner(NULL)
    realState.IsAvaliableToBuy(True)

    board.AddRealStateToBoard(realState)

print(board.GetBoardRealStateList())


# -------> StartGame
playerList = [player1, player2, player3, player4]

# InitRandomPlayerOrder
random.shuffle(playerList)

# Main execution
#while len(playerList)!=1:
#    dd=2

# ThrowDice()
diceFace = np.random.randint(low=1, high=6)

print(diceFace)


for i in board.GetBoardRealStateList():
    boardRealState = i.GetCostOfSale()
    print(boardRealState)
