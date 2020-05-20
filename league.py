import team
import player
import pickle
import league
import time
import random
# FYI you don't need both of the above two lines, only choose
# one. If you want to import choice and randint, then you can do
# from random import choice, randint
# I am back in now though!
pitchers = ['Joe', 'Jim', 'Bob','Jimbob','Bob. Jr','Bobjim']
innings = {
  1: "first",
  2: "second",
  3: "third",
  4: "fourth",
  5: "fifth",
  6: "sixth",
  7: "seventh",
  8: "eighth",
  9: "ninth"
}

class League:
  def __init__(self, name):
    self.name = name
    self.teams = []

  def add_team(self, team):
    self.teams.append(team)
  
  # old/unused function
  def load_data_text(self):
    f = open("leagues.txt","r")
    for line in f:
      teamname, players = line.rstrip().split(":")
      newteam = team.Team(teamname)
      self.teams.append(newteam)
      for player in players:
        newteam.players.append(player)


class Store:
  def __init__(self):
    self.stuff = []
    
  def save_data_store_text(self):
    f = open("store.txt","w")
    for team in league.league.teams:
      for thing in self.stuff:
        f.write(player.thing)


class Equipment:
  def __init__(self, name):
    self.name = name


class Bat(Equipment):
  def __init__(self, material="metal"):
    self.material = material


class Glove(Equipment):
  def __init__(self, glovetype):
    self.glovetype = glovetype 


def playgame():
  for i, team in enumerate(brosleague.teams):
    print(f"{i+1}. {team.name}")
  team1 = int(input("Choose first team to play: "))
  team1 = brosleague.teams[team1-1]
  team2 = int(input("Choose second team to play: "))
  team2 = brosleague.teams[team2-1]
  #start_game = input("Do you want to start the game?(y,n)")
  #if start_game == ['N', 'n', 'no', 'No', 'nO', 'NO', 'q', 'Q']:
  #  print("Ok, ending game")
  #if start_game == ['y', 'Y', 'yes', 'YES', 'Yes']:
  #  print("Starting the game...")
  #  time.sleep("5")

  print(f"It's on! {team1.name} versus {team2.name}!")
  time.sleep(1)
  gameover = False
  for inning in range(1,10):
    for side in ("top","bottom"):
      if side == "top":
        team_at_bat = team1
        team_in_field = team2
      else:
        team_at_bat = team2
        team_in_field = team1
      pitcher = random.choice(pitchers)
      print(f"*** It's the {side} of the {innings[inning]}! ***")
      print(f"At bat: {team_at_bat.name}")
      print(f"In the field: {team_in_field.name}")
      print(f"Now pitching: {pitcher}")
      outs = 0
      while outs < 3:
        batter = team_at_bat.players[team_at_bat.batter]
        print(30*'-')
        print(f"Up to bat: {batter.name}")
        input("(Hit enter key to swing)")
        nextup = False
        strikes = 0
        while not nextup:
          outcome = batter.swing()
          print(f"{batter.name} swings...{outcome}!")
          if outcome == "strike":
            strikes += 1
          if strikes == 3:
            outs += 1
            nextup = True
          if outcome == "out":
            outs += 1
          if outcome in ("single","double","triple","home run","out"):
            nextup = True
        team_at_bat.batter = (team_at_bat.batter + 1) % len(team_at_bat.players)
      print("*** Get yer butts out of the dugout!! Now get out there and win! ***")

f = open("data/league.db",'rb')
brosleague = pickle.load(f)
f.close()
