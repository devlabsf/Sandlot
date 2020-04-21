import team
import player

class League:
  
  def __init__(self, name):
    self.name = name
    self.teams = []

  def add_team(self, team):
    self.teams.append(team)

'''
once we can write the data to a file,
we should replace the below code so that 
we read in the file data...instead 
of reinitializing it from scratch every time!
'''
league = League("DevLabBros League")
team1 = team.Team("Giants")
team2 = team.Team("Dodgers")
league.add_team(team1)
league.add_team(team2)
p1 = player.Player("Jayden","8","first base")
p4 = player.Player("Lazlo","888","shortstop")
p3 = player.Player("Harry","14","pitcher")
p2 = player.Player("John","6","umpire")
team1.add_player(p1)
team1.add_player(p2)
team1.add_player(p3)
team1.add_player(p4)

p1 = player.Player("Joe","69","First Base")
p4 = player.Player("Jim","14","shortstop")
p3 = player.Player("Jack","123","pitcher")
team2.add_player(p1)
team2.add_player(p2)
team2.add_player(p3)