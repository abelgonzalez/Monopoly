
import math
from unicodedata import decimal
from Player import Player


class CautiousPlayer(Player):

    def BuyRealState(self, realStateCost):
        if (self.CheckBalance() - realStateCost > 80):
            self.WithdrawMoney(realStateCost)


player3 = CautiousPlayer()

player3.SetName("Jogador3 - Cauteloso")
print(player3.GetName())

print(player3.CheckBalance())

realStateCost = 60
player3.BuyRealState(realStateCost)

print(player3.CheckBalance())
