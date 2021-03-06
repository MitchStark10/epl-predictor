from stats.ExhaustionStat import ExhaustionStat
from stats.PossessionStat import PossessionStat
from stats.AttackStat import AttackStat
from stats.HomeFieldAdvStat import HomeFieldAdvStat
from stats.DefenseStat import DefenseStat
from stats.CounterAttackStat import CounterAttackStat

class PredictionService:

    statServices = [ExhaustionStat(), PossessionStat(), AttackStat(), HomeFieldAdvStat(), DefenseStat(), CounterAttackStat()]

    #Method Logic: Loop through each statService with the game to get a value
    #Positive value will favor the home team
    #Negative value will favor the away team
    #Final magnitude should represent goal differential
    def predictGame(self, game, databaseConnector):
        goalDifferential = 0
        for statService in self.statServices:
            goalDifferential += statService.getWeightedStat(game, databaseConnector)
        print("Goal Differential for Game " + game.getEspnGameId() + ": " + str(goalDifferential))
        return goalDifferential