import random


class Player(object):

    def __init__(self):
        # Let's add some data to the [instance of the] class.
        self.name = ""
        self.accountBalance = float(300)
        self.realStateList = []

    def GetName(self):
        return self.name

    def SetName(self, name: str):
        self.name = name

    def CheckBalance(self):
        return self.accountBalance

    def AddBalance(self, amount: float):
        self.accountBalance += amount

    def WithdrawMoney(self, amount: float):
        self.accountBalance -= amount

    def DeclareBankrupt(self):
        for i in self.realStateList:
            i.SetOwner("")

        self.realStateList = []

    def AddRealStateOwnership(self, realState):
        self.realStateList.append(realState)

    def GetPlayerByName(player, playerList: list):
        indexPlayer = playerList.index(player)
        return playerList[indexPlayer]


class CautiousPlayer(Player):

    def BuyRealState(self, realState):
        if ((self.CheckBalance() - realState.GetCostOfSale()) > 80):
            self.WithdrawMoney(realState.GetCostOfSale())
            self.AddRealStateOwnership(realState)


class DemandingPlayer(Player):

    def BuyRealState(self, realState):
        if (realState.GetRentalAmount() > 50):
            self.WithdrawMoney(realState.GetRentalAmount())


class RandomPlayer(Player):

    def BuyRealState(self, realState):
        if (random.choice([True, False]) == True):
            self.WithdrawMoney(realState.GetCostOfSale())


class ImpulsivePlayer(Player):

    def BuyRealState(self, realState):
        if (realState.GetCostOfSale() <= self.CheckBalance()):
            self.WithdrawMoney(realState.GetCostOfSale())
