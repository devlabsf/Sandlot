import random
import player
import time

class Team2:

  def __init__(self, name):
    self.name = name
    self.players = []
    self.xp = 0

  def add_player(self, player):
    self.players.append(player)
  
  def delete_player(self, player_name):
    pass

  def team_manager(self, name, boss_level):
    self.manager_name = name
    self.boss_level = 5

  def batting(self, hits):
    if store.gloves == True: 
      if hits == 1 or 2 or 3:
          print("You hit a ball!")
          self.xp+=4

          
          if hits == 4 or 5 or 6:
            print("Strike!")
            self.xp=self.xp+3
          if hits == 7 or 8 or 9:
            print("You hit a single")
            self.xp= self.xp+20
          if hits == 10 or 11:
            print ("You hit a double")
            self.xp=self.xp+40
          if hits == 12:
            print("You hit a triple")
            self.xp=self.xp+100
          if hits == 13:
            print("You hit a Home Run!")
            self.xp=self.xp+80


    else:
      hits = random.randint(5,30)
      self.hits = hits
      hits = random.randint(1,13)
      if hits == 1 or 2 or 3:
        print("You hit a ball!")
        self.xp+=1

        
      if hits == 4 or 5 or 6:
        print("Strike!")
        self.xp=self.xp+0
      if hits == 7 or 8 or 9:
        print("You hit a single")
        self.xp= self.xp+10
      if hits == 10 or 11:
        print ("You hit a double")
        self.xp=self.xp+20
      if hits == 12:
        print("You hit a triple")
        self.xp=self.xp+50
      if hits == 13:
        print("You hit a Home Run!")
        self.xp=self.xp+40
  def set_fielding(self, player_name, pitch_catches, pitch_pitches, catch_catches, catch_first, catch_second, catch_throws, in_throws, in_grounders, in_catches, out_flyballs, out_catches, out_big_throws, out_throws, out_grounders):
    pitcher_catches = random.randint(5,30)
    pitcher_pitches = random.randint(50,100)
    self.pitch_catches = pitcher_catches
    self.pitch_pitches = pitcher_pitches
    catcher_catches = random.randint(50,100)
    catcher_1st = random.randint(5,20)
    catcher_2nd = random.randint(20,50)
    catcher_throws = random.randint(30,50)
    self.catch_catches = catcher_catches
    self.catch_first = catcher_1st
    self.catch_second = catcher_2nd
    self.catch_throws= catcher_throws
    infield_throws = random.randint(50,80)
    infield_grounders = random.randint(50,80)
    infield_catches = random.randint(50,80)
    self.in_throws = infield_throws
    self.in_grounders = infield_grounders
    self.in_catches = infield_catches
    outfield_flyballs = random.randint(50,90)
    outfield_catches = random.randint(50,90)
    outfield_big_throws = random.randint(15,30)
    outfield_throws = random.ranint(50,90)
    outfield_grounders = random.randint(50,90)
    self.out_flyballs = outfield_flyballs
    self.out_catches = outfield_catches
    self.out_big_throws = outfield_big_throws
    self.out_throws = outfield_throws
    self.out_grounders = outfield_grounders