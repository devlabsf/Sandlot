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
import sys
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
def slowprint(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(1./10)
    
def clear():
  sys.stdout.write("\033[2J\033[H")

def save_data():
  f = open("data/league.db",'wb')
  pickle.dump(brosleague,f)
  f.close()
  
def main():
  team = brosleague.teams[0]

  while True:
    print(colored("***************************","yellow"))
    print(colored("**** TEAM MANAGER MENU ****","yellow"))
    print(colored(f" {team.name} ".center(27,'*'),"yellow"))
    print(colored("***************************","yellow"))
    print(colored("a. list player stats", "red"))
    print(colored("b. add player", "yellow"))
    print(colored("c. cut player", "green"))
    print(colored("d. mdify player profile", "blue"))
    print(colored("e. batting practice", "cyan"))
    print(colored("f. trade players", "yellow"))
    print(colored("g. go to store", "green"))
    print(colored("h. select another team", "blue"))
    print(colored("q. quit/save", "red")) 
  
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