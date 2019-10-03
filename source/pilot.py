class Pilot:
    # Empty initializer
    def __init__(self):
        self.setResult(0, 0)

    # Set pilot name
    def setName(self, Name):
        self.Name = Name.upper() # Capitalize name

    # Set pilot's competition ID
    def setPilotID(self, ID):
        self.ID = ID

    # Set nationality
    def setNation(self, nationCode):
        self.Nationality = nationCode

    # Set gender (boolean for female)
    def setGender(self, Female):
        self.Female = (Female != '0')

    # Set birthday
    def setBirthday(self, Born):
        self.Born = Born

    # Set glider
    def setGlider(self, Glider):
        self.Glider = Glider

    # Set pilot sponsors
    def setSponsors(self, Sponsors):
        self.Sponsors = Sponsors

    # Set fai licence validation
    def setFAILicence(self, FAILicence):
        self.validFAI = (FAILicence != '0')

    # Set CIVLID
    def setCIVLID(self, CIVLID):
        self.CIVLID = CIVLID

    # Set result
    def setResult(self, Rank, Points):
        self.Rank = Rank
        self.Points = Points