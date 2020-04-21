import random
import time 
import team


class Store:
  def __init__(self, xp, costamountout, costamountin, stuff):
    self.team.xp    
    self.stuff = stuff 
def save_data_store():
  f = open("store.txt","w")
  for team in league.league.teams:
    for stuff in Store.stuff:
      f.write(player.stuff)

def store_menu():
  costamountoutfield = 10
  costamountinfield = 10
  print("***************************")
  print("This is the store menu")
  time.sleep(0.5)
  print("What would you like to buy?")
  print("(a) Designated hitter")
  print("(b) Bats")
  print("(c) Pitchers")
  print("(d) Gloves")
  print("(e) Upgrade Outfielders")
  print("(f) Upgrade Infielders")
  print("***************************")
  store_choice = input("Your choice")
  print("***************************")
  if store_choice in ['a', 'A']:
    print("Designated Hitter cost: 40xp")
    if team.xp < 40:
      print("Sorry, you don't have enough to pay for this.")
    else:
      team.xp-= 40
      print("")
  if store_choice in ['b', 'B']:
    print("Bats cost: 12xp")
    if bats == True:
      print("Sorry you cant buy this. You already have it")
    if team.xp < 12:
      print("Sorry, you don't have enough to pay for this.")
      bats = False
    else:
      team.xp-= 12
      print("You got your team bats.")
      bats = True
       
    if store_choice in ['d', 'D']:
      if gloves == True:
        print("Sorry you cant buy this. You already have it")
      print("Gloves cost: 5xp")
      if team.xp < 5:
        print("Sorry, you don't have enough to pay for this.")
        gloves = False
    
      else:
        team.xp-=5
        print("You got your team gloves!")
        gloves = True
    
  if store_choice in ['e', 'E']:
    print(f"To upgrade outfielders cost: {costamountoutfield} xp")
    if team.xp < 10:
      print("Sorry, you don't have enough to pay for this.")   
    else:
      costamountoutfield =+ 10
  if store_choice in ['f', 'F']:
    print(f"To upgrade infielders cost: {costamountinfield} xp")
    if team.xp < 10:
      print("Sorry, you don't have enough to pay for this.")
    else:
      costamountinfield=+10
    
