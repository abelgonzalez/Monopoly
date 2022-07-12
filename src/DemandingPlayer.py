
import math
from unicodedata import decimal
from Player import Player


class DemandingPlayer(Player):

    def BuyRealState(self, rentalAmount):
        if (rentalAmount > 50):
            self.WithdrawMoney(rentalAmount)


player2 = DemandingPlayer()

player2.SetName("Jogador2 - Exigente")
print(player2.GetName())

print(player2.CheckBalance())

rentalAmount = 60
player2.BuyRealState(rentalAmount)

print(player2.CheckBalance())
