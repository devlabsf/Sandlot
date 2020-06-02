from termcolor import colored
from random import choice
from time import sleep

from utils import *


class Player:

  def __init__(self, name, number, position):
    self.name = name
    self.number = number
    self.position = position
    self.hits = 0
    self.homeruns = 0
    self.avg = 0.0
    self.era = 0.0
    self.rbi = 0.0
    self.xp = 0
    self.likes = []

  def modify(self):
    ch = input("Change player name?(y,n) ")
    if ch in ['y','Y','yes','YES']:
      name = input("Enter new name: ")
      self.name = name
    ch = input("Change player number?(y,n) ")
    if ch in ['y','Y','yes','YES']:
      num = int(input("Enter new number: "))
      self.number = num
    ch = input("Change player position?(y,n) ")
    if ch in ['y','Y','yes','YES']:
      while True:
        for i, item in enumerate(positions):
          print(f"{i+1}. {item}")
        pos = int(input("Enter new position: "))
        if pos not in range(len(positions)+1):
          print("You cheater muffin! That's not a position!")
        else:
          break
      self.position = positions[pos-1]
    ch = input("Add a player's like? ")
    if ch in ['y','Y','yes','YES']:
      item = input("Add a new player like: ")
      self.likes.append(item)

  def rename(self, name):
    self.name = name

  def update_stats(self, outcome):
   # Jayden/Harry/Lazlo, you'll want to calculate batting avg, ERA, RBI, etc here.
    #for example:
    if outcome in ("single", "double", "triple", "home run"):
      self.hits += 1
    if outcome == "home run":
      self.homeruns += 1

  """ 
  add more stats to player's display 
  """
  def stats(self):
    print("------------------------")
    print("Name:", self.name)
    print("Number:", self.number)
    print("Position:", self.position)
    print("Hits:", self.hits)
    print("Homeruns:", self.homeruns)
    print("Experience:", self.xp)
