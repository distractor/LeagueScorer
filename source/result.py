class Result:
    # -1 for DID NOT FLY
    def __init__(self, Points, Rank):
        self.Points = Points
        self.Rank = Rank

    def setTotalPoints(self, Points):
        self.totalPoints = Points

    def setPoints(self, Points):
        self.Points = Points