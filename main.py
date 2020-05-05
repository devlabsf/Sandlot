"""
OOP FANTASY BASEBALL LEAGUE
TO DO LIST:
* batting practice
* check fielding practice
* trade players
* store is WORKING but not all parts are tested
  --> I moved store_menu() to the team file.
* eventually, teams will play each other
* need to save + load player/team/league data from file
"""
import time
import team
from league import *
from termcolor import colored
#import game

print("***************************")
print("This code is a production of the DL bros".center(27,'*'))
print("***************************")
time.sleep(0.5)
print("Harry's signature\U0001f3c6  ".center(27,'*'))
print("***************************")
time.sleep(0.5)
print("Jayden's signature\U0001f48e  ".center(27,'*'))
print("***************************")
time.sleep(0.5)
print("Lazlo's signature\u2b50  ".center(27,'*'))
print("***************************")
print(" ")

def save_data():
  # write league data
  f = open("leagues.txt","w")
  for team in league.teams:
    f.write(team.name)
    for player in team.players:
      f.write(player.name)
  
def main():
  """
  we'll need to load data here, before main loop starts. For now we're using dummy data, and default is to select the first team in the league.
  """
  #brosleague = league.League("DevLabBros League")
  # don't load yet; load_data() is not working
  #brosleague.load_data()
  #brosleage = league.league
  team = brosleague.teams[0]

  while True:
    print(colored("***************************","yellow"))
    print(colored("**** TEAM MANAGER MENU ****","yellow"))
    print(colored(f" {team.name} ".center(27,'*'),"yellow"))
    print(colored("***************************","yellow"))
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
      if team.dh:
        print("---------------------------")
        print(f"Designated hitter: {team.dh}")
      print("")
    if option in ['b','B']:
      team.add_player()
    if option in ['c','C']:
      team.cut_player()
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
      team.go_to_store()
    if option in ['h','H']:
      for i, team in enumerate(brosleague.teams):
        print(f"{i+1}. {team.name}")
      inter = int(input("Select which team? "))
      team = brosleague.teams[inter-1]
      var=(inter)
    
    if option in ['q','Q']:
      yn = input("Now quitting...Save changes? (y/n) ")
      if yn not in ['n','N','q','Q','NO','no', 'No']:
        save_data()
      break

if __name__ == '__main__':
  main()