from source.result import Result

class Pilot:
    # Empty initializer
    def __init__(self):
        self.Result = []

    def setFinalResult(self, Result):
        self.finalResult = Result

    # Set pilot name
    def setName(self, Name):
        _Name = Name
        _Name = _Name.upper()                   # Capital letters
        _Name = ' '.join(_Name.split())         # Remove additional spaces
        # Remove šumniki
        _Name = _Name.replace('Č', 'C')
        _Name = _Name.replace('Ć', 'C')
        _Name = _Name.replace('Š', 'S')
        _Name = _Name.replace('Ž', 'Z')
        self.Name = _Name

    # Set pilot's competition ID
    def setPilotID(self, ID):
        self.ID = ID

    # Set nationality
    def setNation(self, nationCode):
        self.Nationality = nationCode

    # Set gender (boolean for female)
    # def setGender(self, Female):
    #     self.Female = (Female != '0')

    # Set birthday
    # def setBirthday(self, Born):
    #     self.Born = Born

    # Set glider
    # def setGlider(self, Glider):
    #     self.Glider = Glider

    # Set pilot sponsors
    # def setSponsors(self, Sponsors):
    #     self.Sponsors = Sponsors

    # Set fai licence validation
    # def setFAILicence(self, FAILicence):
    #     self.validFAI = (FAILicence != '0')

    # Set CIVLID
    # def setCIVLID(self, CIVLID):
    #     self.CIVLID = CIVLID

    # Set result
    # def addResult(self, Result):
    #     self.Result.append(Result)

    # def setResult(self, Result):
    #     self.Result = []
    #     self.addResult(Result)