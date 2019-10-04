from source.pilot import Pilot
from source.result import Result

class Scoring:
    def __init__(self, Pilots, Type, Scale):
        self.Pilots = Pilots
        self.Type = Type
        self.Scale = Scale

    def Score(self):
        if (self.Type == 'default'):
            return self.defaultScoring()
        else:
            return self.motoGPScoring()


    # default scoring returns array of pilots
    def defaultScoring(self):
        self.orderPilotsByPoints()
        self.addPilotRank()

        if self.Scale:
            self.rescaleScore()

        return self.Pilots

    def rescaleScore(self):
        self.orderPilotsByPoints()
        if self.Pilots[0].Result[0].Points > 500:
            factor = 1000 / self.Pilots[0].Result[0].Points
        elif self.Pilots[0].Result[0].Points > 250:
            factor = 500 / self.Pilots[0].Result[0].Points
        else:
            factor = 250 / self.Pilots[0].Result[0].Points

        for p in self.Pilots:
            p.setResult(Result(p.Result[0].Points * factor, p.Result[0].Rank))

    # order pilots by points
    def orderPilotsByPoints(self):
        ordered = False
        while (not ordered):
            ordered = True
            for i in range(1, len(self.Pilots)):
                currentPilot = self.Pilots[i]
                previousPilot = self.Pilots[i - 1]

                if (currentPilot.Result[0].Points > previousPilot.Result[0].Points):
                    self.Pilots[i] = previousPilot
                    self.Pilots[i - 1] = currentPilot
                    ordered = False

    # Add rank to pilots
    def addPilotRank(self):
        self.Pilots[0].Result[0].setRank(1)  # winner
        for i in range(1, len(self.Pilots)):
            if (self.Pilots[i].Result[0].Points == self.Pilots[i - 1].Result[0].Points):
                # Same points for two (or more) pilots
                self.Pilots[i].Result[0].setRank(self.Pilots[i - 1].Result[0].Rank)
            else:
                self.Pilots[i].Result[0].setRank(i + 1)

    # Sum points in results:
    def sumPoints(self):
        for pilot in self.Pilots:
            val = 0
            for result in pilot.Result:
                val = val + result.Points

            pilot.setResult(Result(val, 0))

        return self.Pilots