"""
FANTASY BASEBALL LEAGUE
100% object-oriented
TO DO LIST:
* add player
* cut player
* modify player profile
* batting practice
* check fielding practice
* trade players
* go to store
* eventually, teams will play each other
* save and load player/team/league data from file
"""

import random
import time

import team
import player
import league


print("***************************")
print("This code is a production of the DL bros".center(27,'*'))
print("***************************")
time.sleep(1)
print("Harry's signature\U0001f3c6  ".center(27,'*'))
print("***************************")
time.sleep(1)
print("Jayden's signature\U0001f48e  ".center(27,'*'))
print("***************************")
time.sleep(1)
print("Lazlo's signature\u2b50  ".center(27,'*'))
print("***************************")
print(" ")
def save_data():
  f = open("saved.txt","w")
  for team in league.league.teams:
    f.write(team.name)
    for player in team.players:
      f.write(player.name)
  
def main():
  """
  we'll need to load data here, before main loop starts.
  For now we're using dummy data, and default is to
  select the first team in the league.
  """
  team = league.league.teams[0]
  while True:
    print("***************************")
    print("**** TEAM MANAGER MENU ****")
    print(f" {team.name} ".center(27,'*'))
    print("***************************")
    print("a. list player stats")
    print("b. add player")
    print("c. cut player")
    print("d. modify player profile")
    print("e. batting practice")
    print("f. trade players")
    print("g. go to store")
    print("h. select another team")
    print("q. quit/save")  
  
    option = input("Pick one: ")
    if option in ['a','A']:
      for player in team.players:
        player.stats()
    if option in ['b','B']:
      print("We'll add a player here")
    if option in ['c','C']:
      print("We'll delete a player here")
    if option in ['d','D']:
      print("Modify which player?" )
      for i, player in enumerate(team.players):
        print(f"{i+1}. {player.name}")
      ch = int(input("Your choice: " ))
      player = team.players[ch-1]
      player.modify()
    if option in ['e','E']:
      print("batting practice goes here")
    if option in ['f','F']:
      print("trade players")
    if option in ['g','G']:
      pass
      store.store_menu()
    if option in ['h','H']:
      for i, team in enumerate(league.league.teams):
        print(f"{i+1}. {team.name}")
      inter = int(input("Select which team? "))
      team = league.league.teams[inter-1]
      var=(inter)
    
    if option in ['q','Q']:
      yn = input("Now quitting...Save changes? (y/n) ")
      if yn not in ['n','N','q','Q','NO','no', 'No']:
        save_data()

if __name__ == '__main__':
  main()