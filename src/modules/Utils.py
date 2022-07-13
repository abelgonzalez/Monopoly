from modules.Player import Player


def GetPlayerByName(player: Player, playerList: list):
        indexPlayer = playerList.index(player)
        return playerList[indexPlayer]