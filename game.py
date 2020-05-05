import random
import time
import store 
import team
import team2
import player
import league

base1 = False
base2 = False
base3 = False
strikes = 0
team1score = 0
team2score = 0
class Game:

  def __init__(self, team1, team2):
    self.team1 = team1.name
    self.team2 = team2.name

  def game():
    boh = random.randint(1,2)
    if boh == 1:
      print("You got unlucky. You are hitting! ")
    if boh == 2:
      print("You got lucky. You are pitching! ")
    hits = random.randint(1,14)
    if hits == 1 or 2 or 3:
      print("You hit a ball!")
      team.xp+=4
    if hits == 4 or 5 or 6:
      print("Strike!")
    if hits == 7 or 8 or 9:
      print("You hit a single") 
    if hits == 10 or 11:
      print ("You hit a double")
    if hits == 12:
      print("You hit a triple")          
    if hits == 13:
        print("You hit a Home Run!")
       
  print("This is where you will play against other teams in your league.")
  qwerty = input ("Do you want to play? ")
  if qwerty == ['yes', 'Yes', 'y', 'Y']:
    game()
  if qwerty == ['No', 'no', 'n', 'N']:
    print("Goodbye have a good game!")