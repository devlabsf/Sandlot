import team
import store
import player
import pickle

class League:
  
  def __init__(self, name):
    self.name = name
    self.teams = []

  def add_team(self, team):
    self.teams.append(team)
  
  def load_data(self):
    f = open("leagues.txt","r")
    for line in f:
      teamname, players = line.rstrip().split(":")
      newteam = team.Team(teamname)
      self.teams.append(newteam)
      for player in players:
        newteam.players.append(player)

'''
once we can write the data to a file,
we should replace the below code so that 
we read in the file data...instead 
of reinitializing it from scratch every time!
'''

#brosleague = League("DevLabBros League")
#brosleague.add_team(team.Team("Giants"))
#brosleague.add_team(team.Team("Dodgers"))
#brosleague.teams[0].add_to_roster(player.Player("Jayden","8","first base"))
#brosleague.teams[0].add_to_roster(player.Player("John","6","umpire"))
#brosleague.teams[0].add_to_roster(player.Player("Harry","14","pitcher"))
#brosleague.teams[0].add_to_roster(player.Player("Lazlo","888","shortstop"))
#brosleague.teams[1].add_to_roster(player.Player("Joe","69","First Base"))
#brosleague.teams[1].add_to_roster(player.Player("Joe","69","First Base"))
#brosleague.teams[1].add_to_roster(player.Player("Jack","123","pitcher"))

store = store.Store()
f = open("league.db",'rb')
brosleague = pickle.load(f)
f.close()

f = open("league.db",'wb')
pickle.dump(brosleague,f)
f.close()