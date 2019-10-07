import xml.etree.ElementTree as ET
from source.pilot import Pilot
from source.task import Task
from source.result import Result

class FSDB:
    # Initializer
    def __init__(self, filePath):
        self.fsdbFile = ET.parse(filePath).getroot()

    # Gets competition name
    def getCompetitionName(self):
        comp = self.fsdbFile.find('FsCompetition')
        return comp.get('name')

    # Gets competition dates
    def getCompetitionDates(self):
        comp = self.fsdbFile.find('FsCompetition')
        return [comp.get('from'), comp.get('to')]

    # Gets competition location
    def getCompetitionLocation(self):
        comp = self.fsdbFile.find('FsCompetition')
        return comp.get('location')

    # Gets comp participants
    def getCompetitionParticipants(self):
        pilots = [] # List of pilots in the competition
        for child in self.fsdbFile.find('FsCompetition/FsParticipants'):
            p = Pilot()                                         # Initialize class
            p.setPilotID(int(child.get('id')))                  # Set pilot ID
            p.setName(child.get('name'))                        # Set pilot name
            p.setNation(child.get('nat_code_3166_a3'))          # Set pilot nation
            #p.setGender(child.get('female'))               # Set pilot gender
            #p.setBirthday(child.get('birthday'))                # Set pilot birthday
            #p.setGlider(child.get('glider'))                    # Set pilot glider
            #p.setSponsors(child.get('sponsor'))                 # Set pilot sponsors
            #p.setFAILicence(child.get('fai_licence'))           # Set FAI licence validity
            #p.setCIVLID(child.get('CIVLID'))                    # Set pilot CIVLID
            pilots.append(p)                  # Append participant to pilots list

        return pilots

    # Gets task participants and their result (rank, points)
    def getTaskParticipants(self, taskParticipants):
        pilots = [] # List of pilots in the competition
        for child in taskParticipants:
            p = Pilot()                          # Initialize class
            p.setPilotID(int(child.get('id')))   # Set pilot ID

            if (len(child) != 0):
                pilotResult = child.find('FsResult')
                Points = int(pilotResult.get('points'))
                Rank = int(pilotResult.get('rank'))
                p.Result = Result(Points, Rank)     # Set pilot task result
            else:
                p.Result = Result(-1, -1)
            pilots.append(p)  # Append participant to pilots list

        return pilots

    # Gets competition tasks ID, name and participants
    def getCompetitionTasks(self):
        tasks = [] # List of tasks in the competition
        for child in self.fsdbFile.find('FsCompetition/FsTasks'):
            t = Task(int(child.get('id')), child.get('name'))

            # Task waypoints
            #for turnpoint in child.find('FsTaskDefinition'):
            #    print(turnpoint.tag, turnpoint.attrib)

            # Task pilots and their result
            taskParticipants = child.find('FsParticipants')
            t.setPilots(self.getTaskParticipants(taskParticipants))
            tasks.append(t)

        return tasks