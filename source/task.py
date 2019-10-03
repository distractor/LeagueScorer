class Task:
    # Empty initializer
    def __init__(self):
        pass

    # Set ID
    def setID(self, ID):
        self.ID = ID

    # Set name
    def setName(self, Name):
        self.Name = Name

    # Set pilots
    def setPilots(self, Pilots):
        self.Pilots = Pilots

    # order pilots by points
    def orderPilotsByPoints(self):
        ordered = False
        while (not ordered):
            ordered = True
            for i in range(1, len(self.Pilots)):
                currentPilot = self.Pilots[i]
                previousPilot = self.Pilots[i - 1]

                if (currentPilot.Points > previousPilot.Points):
                    self.Pilots[i] = previousPilot
                    self.Pilots[i - 1] = currentPilot
                    ordered = False

    # Assign rank to pilots
    def setPilotsRank(self):
        self.Pilots[0].Rank = 1 # winner
        for i in range(1, len(self.Pilots)):
            if (self.Pilots[i].Points == self.Pilots[i - 1].Points):
                # Same points for two (or more) pilots
                self.Pilots[i].setResult(self.Pilots[i - 1].Rank, self.Pilots[i].Points)
            else:
                self.Pilots[i].setResult(i + 1, self.Pilots[i].Points)
