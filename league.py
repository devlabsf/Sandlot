import random
import pickle
import time
from termcolor import colored

import team
import player
from utils import *

pitchers = ['Joe', 'Jim', 'Bob','Jimbob','Bob Jr.','Bobjim','Bobby','Bobby Joe','Joe Bob','Jimmy','Bobby Jim']

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
    
  # old (unused) function
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
  time.sleep(0.5)
  for inning in range(1,10):
    for side in ("top","bottom"):
      if side == "top":
        team_at_bat = team1
        team_in_field = team2
      else:
        team_at_bat = team2
        team_in_field = team1
      pitcher = random.choice(pitchers)
      bases = 0b0
      print(50 * '-')
      print(f"{team_at_bat.name}: {team_at_bat.gamescore}  |  {team_in_field.name}: {team_in_field.gamescore}")
      print(50 * '-')
      print(f"* It's the {side} of the {innings[inning]}! *")
      print(f"At bat: {team_at_bat.name}")
      print(f"In the field: {team_in_field.name}")
      print(f"Now pitching: {pitcher}")
      outs = 0
      while outs < 3:
        batter = team_at_bat.players[team_at_bat.batter]
        print(30 * '-')
        print(colored(f"Up to bat: {batter.name}","yellow"))
        print(colored(random.choice(commentary),"cyan"))
        input("(Hit enter key to bat) ")
        nextup = False
        strikes = 0
        while not nextup:
          outcome, xp = swing()
          team_at_bat.xp += xp
          print(f"{batter.name} swings...{outcome}!")
          time.sleep(1)
          if outcome == "strike":
            strikes += 1
          if strikes == 3:
            outs += 1
            nextup = True
          if "out" in outcome:
            outs += 1
          if outcome in ("single","double","triple","home run") or ("out" in outcome):
            nextup = True
          batter.update_stats(outcome)
        if outcome in hit_score:
          bases, runs = calc_bases(bases, outcome)
          if runs:
            print(f"{runs} runs batted in!!")
            team_at_bat.gamescore += runs
          #print(f"Bases: {bin(bases)}")
        report_players_on_base(bases)
        print(f"{outs} outs.")
        team_at_bat.batter = (team_at_bat.batter + 1) % len(team_at_bat.players)
      print("* Get yer butts out of the dugout!! Now get out there and win! *")

f = open("data/league.db",'rb')
brosleague = pickle.load(f)
f.close()