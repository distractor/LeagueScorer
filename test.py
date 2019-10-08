from source.league import League
import os

# Load all competitions
directory = os.getcwd() + '/input/' + str(2019)  # directory with league fsdb files
league = League('SLO LIGA 2019', 2019, 'SLO')    # crate league
league.loadCompetitions()                        # loads competitions (gets pilots, tasks, results)
league.getAllPilots()                            # gets league pilots
league.saveResultsToHTML('default.html')         # saves results to file

print('MOTO GP:')
# socore by place, winner gets 25 points
scoring = [25, 20, 16, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
league.useMotoGPScoring(scoring)     # motogp scoring
league.saveResultsToHTML('motoGP.html')          # save motogp results to file