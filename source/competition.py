from source.FSDB import FSDB
from source.result import Result

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

        self.Pilots = FSDB.getCompetitionParticipants(self.FSDB)    # Gets participants at comp
        self.Tasks = FSDB.getCompetitionTasks(self.FSDB)            # Gets tasks flown at comp
        self.addResultsToPilotsFromTasks()                                   # Assigns results to pilots from tasks

    def addResultsToPilotsFromTasks(self):
        self.numberOfTasks = len(self.Tasks)

        for compPilot in self.Pilots:
            result = []
            for task in self.Tasks:
                # Rank and points
                for taskPilot in task.Pilots:
                    if (compPilot.ID == taskPilot.ID):
                        points = taskPilot.Result.Points
                        rank = taskPilot.Result.Rank
                        result.append(Result(points, rank))

            compPilot.Result = result