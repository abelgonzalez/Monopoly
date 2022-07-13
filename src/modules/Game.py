import time
import random
import numpy as np

from modules.Board import Board
from modules.RealState import RealState
from modules.Utils import GetPlayerByName


class Game(object):

    def __init__(self):
        self.name = ""

    def GetGameName(self):
        return self.name

    def SetGameName(self, name: str):
        self.name = name

    def StartGame(self, playerList: list, board: Board, timeoutValue: int):

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

        # Report vars:
        gamesEndedByTimeOut = 0
        timePerGame = []
        totalTime = 0
        finalPlayerListBeahavior = {}
        finalPlayerProbabilities = {}
        for player in playerList:
            finalPlayerProbabilities[player.GetName()] = 0

        # Begin execution
        while (True):
            print("Board iteration #"+str(quantOfBoardIterations))
            print("Iteration #"+str(quantOfIterationsbyPlayer))

            startTimeExecution = time.time()

            for player in playerList:
                # ThrowDice()
                diceFace = np.random.randint(low=1, high=6)
                print("Current player --> " + player.GetName())
                print("Movements (Dice) --> " + str(diceFace))

                # Update current Player position
                currentPositionOnBoard[indexBoardPlayer] += diceFace

                # In case we arrive to boundaries of game. Ex position 20 of board, then starts
                # at the beggining. Another idea: use linked list.
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
                print("Player balance = "+str(playerBalance))
                realStateCost = currentPositionRealState.GetCostOfSale()
                print("RealStateCost = "+str(realStateCost))
                realStateRent = currentPositionRealState.GetRentalAmount()
                print("RealStateRent = "+str(realStateRent))
                ownerName = str(currentPositionRealState.GetOwner())
                print("Owner of this real state " + ownerName)

                # Has the funds and the real state does not have owner
                if (realStateCost <= playerBalance and currentPositionRealState.GetOwner() == ""):

                    player.BuyRealState(currentPositionRealState)
                    currentPositionRealState.SetOwner(player)
                    print(player.GetName() + " is now the owner of " + ownerName)
                    print("Owner after buy " +
                          str(currentPositionRealState.GetOwner()))

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
                    # Adding firt the player and their balance at the report output
                    finalPlayerListBeahavior[player.GetName(
                    )] = player.CheckBalance()

                    player.DeclareBankrupt()
                    currentPositionRealState.SetOwner("")

                    # Remove all real states from him
                    realStateListTmp = []
                    for realState in board.GetBoardRealStateList():
                        if realState.GetOwner() == player:
                            realState.SetOwner("")
                        realStateListTmp.append(realState)
                    # Update board real state list too
                    board.SetBoardRealStateList(realStateListTmp)

                    print("****Player " + str(player.GetName()) +
                          " had declared is in bankrupt***")

                    # Finally, remove it from game
                    playerList.remove(player)

                    # pass

                # Setting the real state, foreach player considering their departure point
                boardRealStateList[currentPositionOnBoard[indexBoardPlayer]
                                   ] = currentPositionRealState

                # At the end of each execution, each player gains 100
                player.AddBalance(float(100.00))

                print("\n")

            quantOfIterationsbyPlayer += 1

            # Stop conditions
            if len(playerList) == 1:
                print("Simulation ended because we have only one player at board")
                break

            if timeoutValue <= quantOfBoardIterations:
                print("Simulation ended by timeout")
                gamesEndedByTimeOut += 1
                break

        # Pre-ending
        # Q2
        endTimeExecution = time.time()
        totalTime = endTimeExecution - startTimeExecution
        # timePerGame.append(totalTime)

        for player in playerList:
            finalPlayerListBeahavior[player.GetName()] = player.CheckBalance()

            # Q4
            # Sorting winners by Checkg account balance
            # sorted(finalPlayerListBeahavior.values())
        for k in sorted(finalPlayerListBeahavior, key=finalPlayerListBeahavior.get, reverse=True):
            k, finalPlayerListBeahavior[k]

            # Q3
            # Getting the first place for this session
        winningPlayer = str(list(finalPlayerListBeahavior.keys())[0])
        finalPlayerProbabilities[winningPlayer] += 1
        finalPlayerProbabilitiesStr = (str(finalPlayerProbabilities))
        gamesEndedByTimeOutStr = str(gamesEndedByTimeOut)
        timePerGameStr = str(totalTime)

        # print("Total execution time (sec): " + str(totalTime))
        # print("4. Winner behaviour: " + str(finalPlayerListBeahavior))
        # print("4. Winner behaviour: " + str(next(iter((finalPlayerListBeahavior.items())))))
        # total gain / 300 foreach gamer

        print("\n")
        print("Partial game report")
        print("1. Time-out ended game: " + gamesEndedByTimeOutStr)
        print("2. Median time: " + timePerGameStr)
        print("3. Percent of victories by player: " +
              finalPlayerProbabilitiesStr)
        print("4. Winner player behaviour: " + winningPlayer)
        print("5. Wealth per player: " + str(finalPlayerListBeahavior))
        print("6. Wealthy player : " +
              str(next(iter((finalPlayerListBeahavior.items())))))

        print("\n")

        return gamesEndedByTimeOut, totalTime, finalPlayerProbabilities, winningPlayer
