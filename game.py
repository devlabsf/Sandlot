import random
import time
import store 
import team1
import team2
import player
import league

class Game:

  def __init__(self, team1, team2):
    self.team1 = team1.name
    self.team2 = team2.name
  print("This is where you will play against other teams in your league.  ")
  qwerty = input ("Do you want to play? ")
  if qwerty == ['yes', 'Yes', 'y', 'Y']:
    game()

  if qwerty == ['No', 'no', 'n', 'N']:
    print("Goodbye have a good game!")
