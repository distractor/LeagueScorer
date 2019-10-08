class Result:
    # -1 for DID NOT FLY
    def __init__(self, Points, Rank):
        self.Points = Points
        self.Rank = Rank

    # sets points
    def setPoints(self, Points):
        self.Points = Points