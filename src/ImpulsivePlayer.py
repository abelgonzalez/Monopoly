
import math
from unicodedata import decimal
from Player import Player


class ImpulsivePlayer(Player):

    def BuyRealState(self, realStateCost):
        if (realStateCost <= self.CheckBalance()):
            self.WithdrawMoney(realStateCost)


player1 = ImpulsivePlayer()

player1.SetName("Jogador1 - Impulsivo")
print(player1.GetName())

print(player1.CheckBalance())

realStateCost = 200
player1.BuyRealState(realStateCost)

print(player1.CheckBalance())
