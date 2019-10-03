from source.FSDB import FSDB

class Competition:
    # Empty initializer
    def __init__(self):
        pass

    # Load from FSDB file
    def loadFromFSDB(self, filePath):
        print('Loading FSDB file from: %s' % filePath)
        self.fsdbFilePath = filePath                                # Save filePath to class
        self.FSDB = FSDB(self.fsdbFilePath)                         # Create FSDB class

        self.Name = FSDB.getCompetitionName(self.FSDB)              # Get Competition name
        self.Dates = FSDB.getCompetitionDates(self.FSDB)            # Get Competition dates
        self.Location = FSDB.getCompetitionLocation(self.FSDB)      # Get Competition location
        self.FAISanctioned = FSDB.getFAIsanctioning(self.FSDB)      # Boolean for FAI sanctioned comp

        self.Pilots = FSDB.getCompetitionParticipants(self.FSDB)    # Gets participants at comp

        self.Tasks = FSDB.getCompetitionTasks(self.FSDB)            # Gets tasks flown at comp

    # Get competition results
    def getResults(self):
        for pilot in self.Pilots:
            for task in self.Tasks:
                for taskPilot in task.Pilots:
                    if (taskPilot.ID == pilot.ID):
                        pilot.Points = pilot.Points + taskPilot.Points
                        break

        self.orderPilotsByPoints() # order pilot list by points
        self.setPilotsRank()
        print('Warning: Results without FTV factor calculated!')

    # Reorder competition pilots by points
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