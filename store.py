import random
import time 
import player
import league

class Store:
  def __init__(self):
    self.stuff = []
    
  def save_data_store(self):
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


